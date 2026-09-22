from datetime import date
from pydantic import EmailStr, BaseModel, field_validator


class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    birthdate: date

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip()

    @field_validator("password")
    @classmethod
    def password_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Password cannot be empty")
        return v

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    birthdate: date


class CredentialsSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def password_not_empty(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Password cannot be empty")
        return v


class UserResponse(BaseModel):
    id: int
    email: str


class AuthResponse(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str
    token_type: str


class ErrorResponse(BaseModel):
    detail: str
    errors: list = None


class RefreshSchema(BaseModel):
    refresh_token: str


class LogoutAllSchema(BaseModel):
    user_id: int
