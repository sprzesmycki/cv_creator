from typing import Optional

from cv_creator.models.models import User
from cv_creator.serializers.db_serializers_marshmallow import user_schema
from cv_creator.storage.postgres import repository
from cv_creator.storage.postgres.db_models import UserDb


def get_user_by_user_id(user_id: int) -> Optional[User]:
    user_db: UserDb = repository.get_user_by_user_id(user_id)
    if user_db is not None:
        user_dict: dict = user_schema.dump(user_db)
        user: User = User.from_json(user_dict)
        return user
    else:
        return None


def add_user(post_user: User) -> Optional[User]:
    user_db: UserDb = repository.add_user(post_user)
    if user_db is not None:
        user_dict: dict = user_schema.dump(user_db)
        user: User = User.from_json(user_dict)
        return user
    else:
        return None


def update_user(user_id: int, patch_user: User) -> Optional[User]:
    user_db: UserDb = repository.get_user_by_user_id(user_id)
    if user_db is not None:
        user_db = repository.update_user(patch_user, user_db, user_id)
        user_dict: dict = user_schema.dump(user_db)
        user: User = User.from_json(user_dict)
        return user
    else:
        return None


def delete_user(user_id: int):
    user_db: UserDb = repository.get_user_by_user_id(user_id)
    if user_db is not None:
        repository.delete_user(user_db)
