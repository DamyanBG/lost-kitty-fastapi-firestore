from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    first_name: str = Field(
        ..., max_length=100, description="First name of the user", example="John"
    )
    last_name: str = Field(
        ..., max_length=100, description="Last name of the user", example="Doe"
    )
    phone_number: str = Field(
        ..., description="Phone number for contact with the user", example="0898000000"
    )
    email: EmailStr = Field(
        ..., description="Email of the user", example="john_doe@example.com"
    )
    password: str = Field(..., description="Password of the user")


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserId(BaseModel):
    id: str


class User(UserBase, UserId):
    pass
