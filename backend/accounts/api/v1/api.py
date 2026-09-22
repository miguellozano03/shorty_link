from datetime import datetime, timedelta, timezone

from django.conf import settings
from ninja import Router

from accounts.services import UserService, TokenService, SesionService
from accounts.exceptions import SessionNotFoundError
from .schemas import CredentialsSchema, AuthResponse, ErrorResponse, RefreshSchema, LogoutAllSchema, RegisterSchema


router = Router(tags=["Auth"])

token_service = TokenService(
    algorithm=settings.ALGORITHM,
    secret_key=settings.SECRET_KEY,
    access_ttl=timedelta(minutes=settings.ACCESS_TTL),
    refresh_ttl=timedelta(days=settings.REFRESH_TTL)
)

session_service = SesionService()

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

@router.post("/register",response={ 200: AuthResponse, 400: ErrorResponse, 409: ErrorResponse})
def register(request, data: RegisterSchema):

    user = UserService.register(
        name=data.name,
        email=data.email,
        password=data.password,
        birthdate=data.birthdate,
    )

    access_token = token_service.create_access_token(user.id)
    refresh_token = token_service.create_refresh_token(user.id)

    expires_at = datetime.fromtimestamp(
        token_service.verify(refresh_token)["exp"],
        tz=timezone.utc,
    )

    session_service.create(
        plain_token=refresh_token,
        user=user,
        expires_at=expires_at,
    )

    return 200, {
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "birthdate": user.birthdate,
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh", response={200: AuthResponse, 400: ErrorResponse})
def refresh(request, data: RefreshSchema):
    payload = token_service.verify(data.refresh_token)
    
    try:
        session = session_service.get(
            plain_token=data.refresh_token
        )
    except SessionNotFoundError:
        return 400, {"detail": "Invalid or revoked refresh token"}

    user = session.user
    session_service.revoke(session=session)

    access_token = token_service.create_access_token(user.id)
    refresh_token = token_service.create_refresh_token(user.id)
    expires_at = datetime.fromtimestamp(
        token_service.verify(refresh_token)["exp"], tz=timezone.utc
    )
    session_service.create(plain_token=refresh_token, user=user, expires_at=expires_at)

    return 200, {
        "user": {"id": user.id, "email": user.email},
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/logout", response={200: dict, 400: ErrorResponse})
def logout(request, data: RefreshSchema):
    session = session_service.get(plain_token=data.refresh_token)
    if session is None:
        return 400, {"detail": "Invalid or revoked refresh token"}

    session_service.revoke(session=session)
    return 200, {"detail": "Logged out"}


@router.post("/logout_all", response={200: dict})
def logout_all(request, data: LogoutAllSchema):
    session_service.revoke_all(user=data.user_id)
    return 200, {"detail": "All sessions revoked"}

