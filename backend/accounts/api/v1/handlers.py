from accounts.exceptions import (
    UserAlreadyExistsError,
    InvalidPasswordError,
    InvalidCredentialsError,
    ValidationError,
)


def user_already_exists_handler(request, exc: UserAlreadyExistsError):
    return {
        "detail": "User with this email already exists",
    }


def invalid_password_handler(request, exc: InvalidPasswordError):
    return {
        "detail": "Invalid password",
        "errors": exc.messages if hasattr(exc, 'messages') else [str(exc)],
    }


def invalid_credentials_handler(request, exc: InvalidCredentialsError):
    return {
        "detail": "Invalid email or password",
    }


def validation_error_handler(request, exc: ValidationError):
    return {
        "detail": "Validation error",
        "errors": exc.messages if hasattr(exc, 'messages') else [str(exc)],
    }