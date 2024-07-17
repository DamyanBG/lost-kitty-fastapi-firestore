from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    token: str


class LoginCredentials(BaseModel):
    email: EmailStr
    password: str
