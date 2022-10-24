from cv_creator.models.models import User
from cv_creator.storage.postgres import repository


def get_user_by_user_id(user_id) -> User:
    return repository.get_user_by_user_id(user_id)


def add_user(post_user) -> User:
    return repository.add_user(post_user)


def update_user(user_id, patch_user) -> User:
    user = repository.get_user_by_user_id(user_id)
    if user is not None:
        return repository.update_user(patch_user, user, user_id)


def delete_user(user_id):
    user = repository.get_user_by_user_id(user_id)
    if user is not None:
        delete_user(user)
