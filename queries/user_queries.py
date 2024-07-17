from typing import Optional
from google.cloud.firestore import FieldFilter

from db import db
from models.user_models import User, UserCreate


user_ref = db.collection("Users")


async def select_user_by_email(email: str) -> Optional[User]:
    filter_by_mail = FieldFilter("email", "==", email)
    query = user_ref.where(filter=filter_by_mail)
    users_docs = [doc async for doc in query.stream()]
    if users_docs:
        user_doc = users_docs[0]
        user_data = user_doc.to_dict()
        user_data["id"] = user_doc.id
        user = User(**user_data)
        return user

    return None


async def insert_user(user: UserCreate) -> User:
    user_data = user.model_dump()
    new_user_ref = user_ref.document()
    await new_user_ref.set(user_data)
    user_data["id"] = new_user_ref.id
    new_user = User(**user_data)
    return new_user
