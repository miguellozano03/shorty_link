from ninja import Router
from datetime import datetime, timedelta, timezone

from accounts.services import UserService, TokenService, SesionService
from .schemas import CredentialsSchema, UserResponse, AuthResponse, ErrorResponse
from django.conf import settings

router = Router(tags=["Auth"])

token_service = TokenService(
    algorithm=settings.ALGORITHM,
    secret_key=settings.SECRET_KEY,
    access_ttl=timedelta(minutes=settings.ACCESS_TTL),
    refresh_ttl=timedelta(days=settings.REFRESH_TTL)
)

session_service = SesionService()


@router.post("/register", response={200: AuthResponse,400: ErrorResponse,409: ErrorResponse})
def register(request, data: CredentialsSchema):
    user = UserService.register(
        email=data.email,
        password=data.password,
    )

    access_token = token_service.create_access_token(user.id)
    refresh_token = token_service.create_refresh_token(user.id)
    
    expires_at = token_service.verify(refresh_token)["exp"]
    session_service.create(plain_token=refresh_token, user=user, expires_at=expires_at)

    return 200, {
        "user": {
            "id": user.id,
            "email": user.email,
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/login", response={200: AuthResponse,400: ErrorResponse})
def login(request, data: CredentialsSchema):
    user = UserService.login(
        email=data.email,
        password=data.password,
    )
    access_token = token_service.create_access_token(user.id)
    refresh_token = token_service.create_refresh_token(user.id)

    payload = token_service.verify(refresh_token)
    expires_at = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)
    session_service.create(plain_token=refresh_token, user=user, expires_at=expires_at)

    return 200, {
        "user": {
            "id": user.id,
            "email": user.email,
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


