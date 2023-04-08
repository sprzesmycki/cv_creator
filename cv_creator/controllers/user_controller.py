from typing import Optional

from cv_creator.models.models import User, UpdateUser
from cv_creator.schema.db_schema.db_serializers import user_db_schema
from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.db_models import UserDb
from cv_creator.storage.postgres.user_repository import UserRepository


def get_user_by_user_id(user_id: int) -> Optional[User]:
    db = SessionLocal()
    user_db: UserDb = UserRepository(db).get_user_by_user_id(user_id)
    if user_db is not None:
        user_dict: dict = user_db_schema.dump(user_db)
        user: User = User(**user_dict)
        return user
    else:
        return None


def add_user(post_user: User) -> User:
    db = SessionLocal()
    user_db: UserDb = UserRepository(db).add_user(post_user)
    user_dict: dict = user_db_schema.dump(user_db)
    user: User = User(**user_dict)
    return user


def update_user(user_id: int, patch_user: UpdateUser) -> Optional[User]:
    db = SessionLocal()
    user_db: UserDb = UserRepository(db).update_user(user_id, patch_user)
    user_dict: dict = user_db_schema.dump(user_db)
    user: User = User(**user_dict)
    return user


def delete_user(user_id: int) -> None:
    db = SessionLocal()
    user_db: UserDb = UserRepository(db).get_user_by_user_id(user_id)
    if user_db is not None:
        UserRepository(db).delete_user(user_db)
