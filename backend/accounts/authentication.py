from django.contrib.auth import get_user_model
from django.conf import settings
from ninja.security import HttpBearer

from accounts.services.token_service import TokenService

User = get_user_model()


class JWTAuth(HttpBearer):

    def authenticate(self, request, token):
        token_service = TokenService(
            algorithm=settings.ALGORITHM,
            secret_key=settings.SECRET_KEY,
            access_ttl=settings.ACCESS_TTL,
            refresh_ttl=settings.REFRESH_TTL
        )

        try:
            payload = token_service.verify(token)
        except ValueError:
            return None

        if payload.get("type") != "access":
            return None

        try:
            return User.objects.get(id=payload["sub"])
        except User.DoesNotExist:
            return None