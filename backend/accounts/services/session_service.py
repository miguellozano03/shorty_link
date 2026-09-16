import hashlib
from datetime import datetime, timezone
from accounts.exceptions import SessionNotFoundError
from accounts.models import Session


class SesionService:
    
    def create(self,*, plain_token: str, user, expires_at: datetime):
        token_hash = hashlib.sha256(plain_token.encode()).hexdigest()

        session = Session(
            user=user,
            token_hash=token_hash,
            expires_at=expires_at
        )
        session.save()
        return session


    def get(self, *, plain_token: str):
        token_hash = hashlib.sha256(plain_token.encode()).hexdigest()

        try:
            return Session.objects.get(token_hash=token_hash)
        except Session.DoesNotExist:
            raise SessionNotFoundError("Session not found")

    def revoke(self,*, session):
        session.revoked_at = timezone.now()
        session.save(update_fields=["revoked_at"])
        return session

    def revoke_all(self, *, user):

        return Session.objects.filter(
            user=user,
            revoked_at__isnull=True,
        ).update(
            revoked_at=timezone.now()
        )

    def exists(self, *, plain_token: str, user):
        token_hash = hashlib.sha256(
            plain_token.encode()
        ).hexdigest()

        return Session.objects.filter(
            token_hash=token_hash,
            user=user,
        ).exists()