from ninja import NinjaAPI
from accounts.api.v1.api import router as accounts_router
from shortener.api.v1.api import router as shortener_router
from accounts.exceptions import (
    UserAlreadyExistsError,
    InvalidPasswordError,
    InvalidCredentialsError,
    ValidationError,
)

api = NinjaAPI(version="1.0.0")


def handle_user_already_exists(request, exc):
    return api.create_response(
        request,
        {"detail": "User with this email already exists"},
        status=409,
    )


def handle_invalid_password(request, exc):
    return api.create_response(
        request,
        {
            "detail": "Invalid password",
            "errors": (
                exc.messages
                if hasattr(exc, "messages")
                else [str(exc)]
            ),
        },
        status=400,
    )


def handle_invalid_credentials(request, exc):
    return api.create_response(
        request,
        {"detail": "Invalid email or password"},
        status=401,
    )


def handle_validation_error(request, exc):
    return api.create_response(
        request,
        {
            "detail": "Validation error",
            "errors": (
                exc.messages
                if hasattr(exc, "messages")
                else [str(exc)]
            ),
        },
        status=400,
    )


api.add_exception_handler(
    UserAlreadyExistsError,
    handle_user_already_exists,
)

api.add_exception_handler(
    InvalidPasswordError,
    handle_invalid_password,
)

api.add_exception_handler(
    InvalidCredentialsError,
    handle_invalid_credentials,
)

api.add_exception_handler(
    ValidationError,
    handle_validation_error,
)

api.add_router("/auth", accounts_router)
api.add_router("/shortener", shortener_router)