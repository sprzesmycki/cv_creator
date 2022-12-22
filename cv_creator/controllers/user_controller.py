from cv_creator.models.models import User
from cv_creator.serializers.db_serializers import CompleteUserSchema
from cv_creator.storage.postgres import repository
from cv_creator.storage.postgres.db_models import UserDb


def get_user_by_user_id(user_id: int) -> User:
    user_db: UserDb = repository.get_user_by_user_id(user_id)
    user_dict = CompleteUserSchema().dump(user_db)
    user = User.Schema().load(user_dict)
    return user


def add_user(post_user: User) -> int:
    user: UserDb = repository.add_user(post_user)
    return user.id


def update_user(user_id: int, patch_user: User) -> User:
    user_db: UserDb = repository.get_user_by_user_id(user_id)
    if user_db is not None:
        user_db = repository.update_user(patch_user, user_db, user_id)
        user_dict = CompleteUserSchema().dump(user_db)
        user = User.Schema().load(user_dict)
        return user


def delete_user(user_id: int):
    user_db: UserDb = repository.get_user_by_user_id(user_id)
    if user_db is not None:
        repository.delete_user(user_db)
