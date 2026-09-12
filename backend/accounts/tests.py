from django.test import TestCase
from django.contrib.auth import get_user_model
from .services import UserService

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

        with self.assertRaises(ValueError):
            UserService().login(email="test@example.com", password="WrongPassword!")