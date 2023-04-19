from typing import Optional

from cv_creator.models.models import User, UpdateUser, UserExperience
from cv_creator.schema.db_schema.db_serializers import user_db_schema
from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.db_models import UserDb, UserExperienceDb
from cv_creator.storage.postgres.user_experience_repository import (
    UserExperienceRepository,
)
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
    else:
        raise ValueError("User does not exist")


def get_user_experience_by_user_id(user_id: int) -> list[UserExperience]:
    db = SessionLocal()
    user_experiences_db: list[UserExperienceDb] = UserExperienceRepository(
        db
    ).get_user_experience_by_user_id(user_id)
    # TODO add conversion to model UserExperience from UserExperienceDb
    user_experiences: list[UserExperience] = []
    return user_experiences


def get_user_experience_by_user_experience_id(
    user_experience_id: int,
) -> UserExperience:
    db = SessionLocal()
    user_experience: UserExperienceDb = UserExperienceRepository(
        db
    ).get_user_experience_by_user_experience_id(user_experience_id)
    # TODO add conversion to model UserExperience from UserExperienceDb
    return user_experience


def add_user_experience(
    user_id: int, user_experience: UserExperience
) -> UserExperience:
    db = SessionLocal()
    user_experience_db: UserExperienceDb = UserExperienceRepository(
        db
    ).add_user_experience(user_id, user_experience)
    # todo missing implementation
    return user_experience


def update_user_experience(
    user_experience_id: int, user_experience: UserExperience
) -> UserExperience:
    db = SessionLocal()
    user_experience_db: UserExperienceDb
    # todo missing implementation
    return user_experience
