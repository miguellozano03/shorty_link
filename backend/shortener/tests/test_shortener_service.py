from unittest.mock import Mock, call, patch

from django.db import IntegrityError
from django.test import TestCase

from shortener.models import Url
from shortener.services.shortener_service import ShortenerService


class ShortenerServiceTests(TestCase):
    def setUp(self):
        self.service = ShortenerService()
        self.user = Mock(id=42)

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_get_returns_url_for_user_and_code(self, get):
        expected = Mock()
        get.return_value = expected

        self.assertIs(self.service.get("abc123", self.user), expected)
        get.assert_called_once_with(code="abc123", user_id=42)

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_get_propagates_not_found(self, get):
        get.side_effect = Url.DoesNotExist

        with self.assertRaises(Url.DoesNotExist):
            self.service.get("missing", self.user)

        get.assert_called_once_with(code="missing", user_id=42)

    @patch("shortener.services.shortener_service.Url.objects.filter")
    def test_get_all_returns_user_urls(self, filter_urls):
        expected = [Mock(), Mock()]
        filter_urls.return_value = expected

        self.assertIs(self.service.get_all(self.user), expected)
        filter_urls.assert_called_once_with(user_id=42)

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_resolve_returns_url_by_code(self, get):
        expected = Mock()
        get.return_value = expected

        self.assertIs(self.service.resolve("abc123"), expected)
        get.assert_called_once_with(code="abc123")

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_resolve_propagates_not_found(self, get):
        get.side_effect = Url.DoesNotExist

        with self.assertRaises(Url.DoesNotExist):
            self.service.resolve("missing")

    @patch("shortener.services.shortener_service.Url.objects.create")
    @patch("shortener.services.shortener_service.generate_short_code", return_value="abc123")
    def test_create_returns_created_url(self, generate_code, create):
        expected = Mock()
        create.return_value = expected

        result = self.service.create("https://example.com", self.user)

        self.assertIs(result, expected)
        generate_code.assert_called_once_with()
        create.assert_called_once_with(
            title=None,
            long_url="https://example.com",
            code="abc123",
            user=self.user,
        )

    @patch("shortener.services.shortener_service.Url.objects.create")
    @patch(
        "shortener.services.shortener_service.generate_short_code",
        side_effect=["duplicate", "unique"],
    )
    def test_create_retries_after_integrity_error(self, generate_code, create):
        expected = Mock()
        create.side_effect = [IntegrityError, expected]

        result = self.service.create("https://example.com")

        self.assertIs(result, expected)
        self.assertEqual(generate_code.call_count, 2)
        self.assertEqual(
            create.call_args_list,
            [
                call(
                    title=None,
                    long_url="https://example.com",
                    code="duplicate",
                    user=None,
                ),
                call(
                    title=None,
                    long_url="https://example.com",
                    code="unique",
                    user=None,
                ),
            ],
        )

    @patch("shortener.services.shortener_service.Url.objects.create", side_effect=IntegrityError)
    @patch("shortener.services.shortener_service.generate_short_code", return_value="duplicate")
    def test_create_raises_after_five_collisions(self, generate_code, create):
        with self.assertRaisesRegex(RuntimeError, "Could not generate a unique short code"):
            self.service.create("https://example.com")

        self.assertEqual(generate_code.call_count, 5)
        self.assertEqual(create.call_count, 5)

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_edit_updates_fields_and_returns_url(self, get):
        url = Mock()
        get.return_value = url

        result = self.service.edit(
            "abc123", self.user, title="Example", long_url="https://new.example"
        )

        self.assertIs(result, url)
        get.assert_called_once_with(code="abc123", user_id=42)
        self.assertEqual(url.title, "Example")
        self.assertEqual(url.long_url, "https://new.example")
        url.save.assert_called_once_with(update_fields=["title", "long_url"])

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_edit_preserves_omitted_fields(self, get):
        url = Mock(title="Existing title", long_url="https://existing.example")
        get.return_value = url

        self.service.edit("abc123", self.user)

        self.assertEqual(url.title, "Existing title")
        self.assertEqual(url.long_url, "https://existing.example")
        url.save.assert_called_once_with(update_fields=["title", "long_url"])

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_edit_propagates_not_found(self, get):
        get.side_effect = Url.DoesNotExist

        with self.assertRaises(Url.DoesNotExist):
            self.service.edit("missing", self.user, title="Example")

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_delete_deletes_url(self, get):
        url = Mock()
        get.return_value = url

        self.service.delete("abc123", self.user)

        get.assert_called_once_with(code="abc123", user_id=42)
        url.delete.assert_called_once_with()

    @patch("shortener.services.shortener_service.Url.objects.get")
    def test_delete_propagates_not_found(self, get):
        get.side_effect = Url.DoesNotExist

        with self.assertRaises(Url.DoesNotExist):
            self.service.delete("missing", self.user)