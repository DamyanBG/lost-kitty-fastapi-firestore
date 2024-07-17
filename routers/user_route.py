from fastapi import APIRouter, HTTPException, status

from models.user_models import User, UserCreate
from models.credentials_models import LoginCredentials, Token
from auth.password import hash_password, check_hashed_password
from auth.token import create_access_token
from queries.user_queries import select_user_by_email, insert_user

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    existing_user = await select_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered!"
        )

    user.password = hash_password(user.password)
    new_user = await insert_user(user)

    return new_user


@user_router.post("/login", response_model=Token)
async def login_user(credentials: LoginCredentials):
    existing_user = await select_user_by_email(credentials.email)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad credentials!"
        )

    if not check_hashed_password(existing_user.password, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad credentials!"
        )

    token = create_access_token(existing_user)

    return {"token": token}
