import mock

from cv_creator.controllers.user_controller import (
    add_user,
    update_user,
    delete_user,
    get_user_by_user_id,
)
from cv_creator.models.models import User, UpdateUser
from cv_creator.storage.postgres.db_models import UserDb


def test_add_user_controller(client):
    user = mock.create_autospec(User)
    user_db = mock.create_autospec(UserDb)
    user_db.id = 17
    user_db.first_name = "seb"
    user_db.last_name = "prz"
    user_db.permission = "admin"

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.add_user",
        return_value=user_db,
    ):
        new_user = add_user(user)

    assert new_user.id == user_db.id
    assert new_user.first_name == user_db.first_name
    assert new_user.last_name == user_db.last_name
    assert new_user.permission == user_db.permission


def test_update_user_controller(client):
    existing_user = User(id=15, first_name="seba", last_name="prze", permission="user")
    patch_user = UpdateUser(first_name="seb", last_name="prz", permission="admin")

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.update_user",
        return_value=patch_user,
    ):
        patched_user_db = update_user(existing_user.id, patch_user)

    assert patched_user_db.first_name == patch_user.first_name
    assert patched_user_db.last_name == patch_user.last_name
    assert patched_user_db.permission == patch_user.permission


def test_update_user_controller_one_field(client):
    existing_user = User(id=15, first_name="seba", last_name="prze", permission="user")
    patch_user = UpdateUser(last_name="prz")

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.update_user",
        return_value=patch_user,
    ):
        patched_user_db = update_user(existing_user.id, patch_user)

    assert patched_user_db.first_name == patch_user.first_name
    assert patched_user_db.last_name == patch_user.last_name
    assert patched_user_db.permission == patch_user.permission


def test_delete_user_controller_none(client):
    user_id = mock.create_autospec(int)

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.get_user_by_user_id",
        return_value=None,
    ):
        with mock.patch(
            "cv_creator.controllers.user_controller.UserRepository.delete_user"
        ) as mock_delete_user:
            delete_user(user_id)

    assert not mock_delete_user.called


def test_delete_user_controller(client):
    user_db = mock.create_autospec(UserDb)
    user_id = mock.create_autospec(int)

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.get_user_by_user_id",
        return_value=user_db,
    ):
        with mock.patch(
            "cv_creator.controllers.user_controller.UserRepository.delete_user"
        ) as mock_delete_user:
            delete_user(user_id)

    assert mock_delete_user.called


def test_get_user_controller_none(client):
    user_id = mock.create_autospec(int)

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.get_user_by_user_id",
        return_value=None,
    ):
        user = get_user_by_user_id(user_id)

    assert user is None


def test_get_user_controller(client):
    user_db = mock.create_autospec(UserDb)
    user_db.first_name = "Rob"
    user_db.last_name = "Son"
    user_id = mock.create_autospec(int)

    with mock.patch(
        "cv_creator.controllers.user_controller.UserRepository.get_user_by_user_id",
        return_value=user_db,
    ):
        user_from_db = get_user_by_user_id(user_id)

    assert user_db.first_name == user_from_db.first_name
    assert user_db.last_name == user_from_db.last_name
