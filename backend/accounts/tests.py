from datetime import timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from .services import UserService, TokenService
from .exceptions import InvalidCredentialsError

User = get_user_model()


class UserServiceTestCase(TestCase):

    def test_register_create_user(self):
        user = UserService().register(
            email="test@example.com",
            password="SuperSecret123!"
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_register_normalize_email(self):
        user = UserService().register(
            email=" TEST@EXAMPLE.com ",
            password="SuperSecret123!"
        )

        self.assertEqual(user.email, "test@example.com")

    def test_login_user(self):
        UserService().register(
            email="test@example.com",
            password="SuperSecret123!"
        )

        user = UserService().login(email="test@example.com", password="SuperSecret123!")
        self.assertEqual(user.email, "test@example.com")

    def test_login_invalid_credentials(self):
        UserService().register(
            email="test@example.com",
            password="SuperSecret123!"
        )

        with self.assertRaises(InvalidCredentialsError):
            UserService().login(email="test@example.com", password="WrongPassword!")


class TokenServiceTest(TestCase):

    def setUp(self):
        self.token_service = TokenService(
            algorithm="HS256",
            secret_key="EIMI9z6P+d7AGyh9FEOe6Q4hzBPkOgL8U9M2HlhDAYVVm3mX+g8n0pRgGeGy6visgb0hDJEELO0Aj4nT9KsrqQ==",
            access_ttl=timedelta(minutes=15),
            refresh_ttl=timedelta(days=1)
        )

    def test_create_access_token(self):
        token = self.token_service.create_access_token(123)

        decoded = self.token_service.verify(token)

        self.assertEqual(decoded["sub"], "123")
        self.assertEqual(decoded["type"], "access")
        self.assertIn("exp", decoded)
        self.assertIn("iat", decoded)


    def test_create_refresh_token(self):
        token = self.token_service.create_refresh_token(123)
        
        decoded = self.token_service.verify(token)

        print(decoded)
        
        self.assertEqual(decoded["sub"], "123")
        self.assertEqual(decoded["type"], "refresh")
        self.assertIn("exp", decoded)
        self.assertIn("iat", decoded)

    # def test_verify_token(self):
    #     pass