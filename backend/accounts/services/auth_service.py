from datetime import date
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password as django_validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from accounts.exceptions import UserAlreadyExistsError, ValidationError, InvalidPasswordError, InvalidCredentialsError

User = get_user_model()

class UserService:

    @staticmethod
    def register(*, name: str, email: str, password: str, birthdate: date):
        if not name or not email or not password or not birthdate:
            raise ValidationError(
                ["Name, email, password and birthdate are required"]
            )

        email = email.strip().lower()
        name = name.strip()

        if User.objects.filter(email=email).exists():
            raise UserAlreadyExistsError()

        try:
            django_validate_password(password)
        except DjangoValidationError as exc:
            raise InvalidPasswordError(exc.messages) from exc

        return User.objects.create_user(
            email=email,
            password=password,
            name=name,
            birthdate=birthdate,
        )

    @staticmethod
    def login(*, email: str, password: str):
        if not email or not password:
            raise ValidationError(["Email and password are required"])
        
        user = authenticate(username=email, password=password)

        if user is None:
            raise InvalidCredentialsError("Invalid email or password")

        return user
