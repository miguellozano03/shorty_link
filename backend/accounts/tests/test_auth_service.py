from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.services import UserService
from accounts.exceptions import InvalidCredentialsError

User = get_user_model()

class UserServiceTestCase(TestCase):

    def test_register_create_user(self):
        user = UserService().register(**{
            "name": "Test User",
            "email": "test@example.com",
            "password": "SuperSecret123!",
            "birthdate": "1990-01-01",
        })

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_register_normalize_email(self):
        user = UserService().register(**{
            "name": "Test User",
            "email": " TEST@EXAMPLE.com ",
            "password": "SuperSecret123!",
            "birthdate": "1990-01-01",
        })

        self.assertEqual(user.email, "test@example.com")

    def test_login_user(self):
        UserService().register(**{
            "name": "Test User",
            "email": "test@example.com",
            "password": "SuperSecret123!",
            "birthdate": "1990-01-01",
        })

        user = UserService().login(email="test@example.com", password="SuperSecret123!")
        self.assertEqual(user.email, "test@example.com")

    def test_login_invalid_credentials(self):
        UserService().register(**{
            "name": "Test User",
            "email": "test@example.com",
            "password": "SuperSecret123!",
            "birthdate": "1990-01-01",
        })

        with self.assertRaises(InvalidCredentialsError):
            UserService().login(email="test@example.com", password="WrongPassword!")
