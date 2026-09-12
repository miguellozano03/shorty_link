from ninja import Router

from accounts.services import UserService
from .schemas import CredentialsSchema, UserResponse, AuthResponse, ErrorResponse

router = Router(tags=["Auth"])


@router.post(
    "/register",
    response={
        200: AuthResponse,
        400: ErrorResponse,
        409: ErrorResponse,
    },
)
def register(request, data: CredentialsSchema):
    user = UserService.register(
        email=data.email,
        password=data.password,
    )

    return 200, {
        "user": {
            "id": user.id,
            "email": user.email,
        },
        "access_token": "...",
        "token_type": "bearer",
    }


@router.post(
    "/login",
    response={
        200: AuthResponse,
        400: ErrorResponse,
    },
)
def login(request, data: CredentialsSchema):
    user = UserService.login(
        email=data.email,
        password=data.password,
    )

    return 200, {
        "user": {
            "id": user.id,
            "email": user.email,
        },
        "access_token": "mock_access_token",
        "token_type": "bearer",
    }


