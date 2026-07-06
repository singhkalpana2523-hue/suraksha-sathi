from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class SignupRequest(BaseModel):
    name: str = Field(..., min_length=3)
    phone: str
    password: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        # Must be a valid 10-digit Indian mobile number starting with 6/7/8/9
        if v is None:
            raise ValueError("Phone number is required")
        v_str = str(v).strip()
        if len(v_str) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        if not v_str.isdigit():
            raise ValueError("Phone number must contain only digits")
        if v_str[0] not in {"6", "7", "8", "9"}:
            raise ValueError("Phone number must start with 6, 7, 8, or 9")
        return v_str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if v is None:
            raise ValueError("Password is required")
        v_str = str(v)
        if len(v_str) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return v_str


class LoginRequest(BaseModel):
    phone: str
    password: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        # Reuse same rules as signup
        if v is None:
            raise ValueError("Phone number is required")
        v_str = str(v).strip()
        if len(v_str) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        if not v_str.isdigit():
            raise ValueError("Phone number must contain only digits")
        if v_str[0] not in {"6", "7", "8", "9"}:
            raise ValueError("Phone number must start with 6, 7, 8, or 9")
        return v_str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if v is None:
            raise ValueError("Password is required")
        v_str = str(v)
        if len(v_str) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return v_str

