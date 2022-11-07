from cv_creator.models.models import User
from cv_creator.storage.postgres import repository
from cv_creator.storage.postgres.db_models import UserDb


def get_user_by_user_id(user_id) -> User:
    user_db = repository.get_user_by_user_id(user_id)
    user = User.Schema().load(user_db)  # todo not tested if this works
    return user


def add_user(post_user) -> User:
    return repository.add_user(post_user)


def update_user(user_id: int, patch_user: User) -> User:
    user: UserDb = repository.get_user_by_user_id(user_id)
    if user is not None:
        return repository.update_user(patch_user, user, user_id)


def delete_user(user_id):
    user = repository.get_user_by_user_id(user_id)
    if user is not None:
        delete_user(user)
