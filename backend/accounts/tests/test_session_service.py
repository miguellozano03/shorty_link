import hashlib
from datetime import date, timedelta

from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.services import SesionService
from accounts.exceptions import SessionNotFoundError

User = get_user_model()

class SessionServiceTest(TestCase):

    def setUp(self):
        self.session_service = SesionService()
        self.user = User.objects.create_user(
            name="Test User",
            email="test@example.com",
            password="SuperSecret123!",
            birthdate=date(1990, 1, 1),
        )
        self.other_user = User.objects.create_user(
            name="Other User",
            email="other@example.com",
            password="SuperSecret123!",
            birthdate=date(1991, 1, 1),
        )
        self.expires_at = timezone.now() + timedelta(days=1)

    # ---- create ----

    def test_create_session(self):
        session = self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )

        self.assertEqual(session.user, self.user)
        self.assertEqual(
            session.token_hash,
            hashlib.sha256(b"token-123").hexdigest(),
        )
        self.assertNotEqual(session.token_hash, "token-123")
        self.assertEqual(session.expires_at, self.expires_at)
        self.assertIsNone(session.revoked_at)

    def test_create_session_with_duplicate_token_fails(self):
        self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )

        with self.assertRaises(IntegrityError):
            self.session_service.create(
                plain_token="token-123",
                user=self.other_user,
                expires_at=self.expires_at,
            )

    # ---- get ----

    def test_get_session(self):
        created_session = self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )

        session = self.session_service.get(plain_token="token-123")

        self.assertEqual(session.pk, created_session.pk)

    def test_get_missing_session_raises_session_not_found(self):
        with self.assertRaises(SessionNotFoundError):
            self.session_service.get(plain_token="missing-token")

    def test_get_expired_session_raises_session_not_found(self):
        self.session_service.create(
            plain_token="expired-token",
            user=self.user,
            expires_at=timezone.now() - timedelta(seconds=1),
        )

        with self.assertRaises(SessionNotFoundError):
            self.session_service.get(plain_token="expired-token")

    def test_get_revoked_session_raises_session_not_found(self):
        session = self.session_service.create(
            plain_token="revoked-token",
            user=self.user,
            expires_at=self.expires_at,
        )
        self.session_service.revoke(session=session)

        with self.assertRaises(SessionNotFoundError):
            self.session_service.get(plain_token="revoked-token")

    # ---- exists ----

    def test_exists_returns_true_for_matching_user_and_token(self):
        self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )

        self.assertTrue(
            self.session_service.exists(
                plain_token="token-123",
                user=self.user,
            )
        )

    def test_exists_returns_false_for_wrong_user_or_token(self):
        self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )

        self.assertFalse(
            self.session_service.exists(
                plain_token="token-123",
                user=self.other_user,
            )
        )
        self.assertFalse(
            self.session_service.exists(
                plain_token="missing-token",
                user=self.user,
            )
        )

    def test_exists_returns_false_for_expired_session(self):
        self.session_service.create(
            plain_token="expired-token",
            user=self.user,
            expires_at=timezone.now() - timedelta(seconds=1),
        )

        self.assertFalse(
            self.session_service.exists(
                plain_token="expired-token",
                user=self.user,
            )
        )

    def test_exists_returns_false_for_revoked_session(self):
        session = self.session_service.create(
            plain_token="revoked-token",
            user=self.user,
            expires_at=self.expires_at,
        )
        self.session_service.revoke(session=session)

        self.assertFalse(
            self.session_service.exists(
                plain_token="revoked-token",
                user=self.user,
            )
        )

    # ---- revoke ----

    def test_revoke_session(self):
        session = self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )

        revoked_session = self.session_service.revoke(session=session)
        session.refresh_from_db()

        self.assertEqual(revoked_session.pk, session.pk)
        self.assertIsNotNone(session.revoked_at)

    def test_revoke_already_revoked_session_keeps_original_timestamp(self):
        session = self.session_service.create(
            plain_token="token-123",
            user=self.user,
            expires_at=self.expires_at,
        )
        self.session_service.revoke(session=session)
        session.refresh_from_db()
        first_revoked_at = session.revoked_at

        self.session_service.revoke(session=session)
        session.refresh_from_db()

        self.assertEqual(session.revoked_at, first_revoked_at)

    # ---- revoke_all ----

    def test_revoke_all_only_revokes_active_sessions_for_user(self):
        active_session = self.session_service.create(
            plain_token="active-token",
            user=self.user,
            expires_at=self.expires_at,
        )
        revoked_session = self.session_service.create(
            plain_token="revoked-token",
            user=self.user,
            expires_at=self.expires_at,
        )
        other_user_session = self.session_service.create(
            plain_token="other-user-token",
            user=self.other_user,
            expires_at=self.expires_at,
        )
        revoked_session.revoked_at = timezone.now()
        revoked_session.save(update_fields=["revoked_at"])

        revoked_count = self.session_service.revoke_all(user=self.user)

        active_session.refresh_from_db()
        revoked_session.refresh_from_db()
        other_user_session.refresh_from_db()

        self.assertEqual(revoked_count, 1)
        self.assertIsNotNone(active_session.revoked_at)
        self.assertIsNotNone(revoked_session.revoked_at)
        self.assertIsNone(other_user_session.revoked_at)

    def test_revoke_all_with_no_active_sessions_returns_zero(self):
        revoked_count = self.session_service.revoke_all(user=self.user)

        self.assertEqual(revoked_count, 0)