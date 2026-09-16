from datetime import datetime, timezone
import jwt

class TokenService:
    def __init__(self, algorithm: str, secret_key: str, access_ttl, refresh_ttl):
        self.algorithm = algorithm
        self.secret_key = secret_key
        self.access_ttl = access_ttl
        self.refresh_ttl = refresh_ttl

    def create_access_token(self, user_id: int):
        now = datetime.now(timezone.utc)

        access_payload = {
            "sub": str(user_id),
            "type": "access",
            "exp": now + self.access_ttl,
            "iat": now
        }

        token = jwt.encode(payload=access_payload, key=self.secret_key, algorithm=self.algorithm)

        return token
    
    def create_refresh_token(self, user_id: int):
        now = datetime.now(timezone.utc)

        refresh_payload = {
            "sub": str(user_id),
            "type": "refresh",
            "exp": now + self.refresh_ttl,
            "iat": now
        }

        token = jwt.encode(payload=refresh_payload, key=self.secret_key, algorithm=self.algorithm)

        return token

    def verify(self, token: str):
        try:
            payload = jwt.decode(token, key=self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidSignatureError:
            raise ValueError("Signature verification failed")
        except jwt.DecodeError:
            raise ValueError("Token is malformed or invalid")
        except jwt.InvalidTokenError:
            raise ValueError("An error occurred while validating the token.")
