import mock
import pytest
from mock import call

from cv_creator.app import create_app
from cv_creator.controllers.user_controller import add_user, update_user, delete_user, get_user_by_user_id
from cv_creator.models.models import User, UpdateUser
from cv_creator.storage.postgres.db_models import UserDb


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_get_user_method_calls(client):
    with mock.patch("cv_creator.routes.get_user_by_user_id") as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.get("/user?user_id=99")

    assert get_user_by_user_id_mock.called
    assert get_user_by_user_id_mock.call_args == call(99)
    assert not add_user_mock.called
    assert not update_user_mock.called
    assert not delete_user_mock.called


def test_post_user_method_calls(client):
    with mock.patch("cv_creator.routes.get_user_by_user_id") as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.post("/user", json={
                        "first_name": "seb",
                        "last_name": "as",
                        "permission": "admin",
                        "user_skills": [
                            {
                                "skill": {
                                    "id": 0,
                                    "skill_name": "Nunu"
                                },
                                "skill_level": 3
                            }
                        ],
                        "user_experience": []
                    })

    assert add_user_mock.called
    assert not get_user_by_user_id_mock.called
    assert not update_user_mock.called
    assert not delete_user_mock.called


def test_patch_user_method_calls(client):
    with mock.patch("cv_creator.routes.get_user_by_user_id") as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.patch("/user?user_id=99", json={
                        "first_name": "huhhfffdfgfgfue",
                        "id": "22",
                        "last_name": "sebzodfdfnek"
                    })

    assert not add_user_mock.called
    assert get_user_by_user_id_mock.called
    assert update_user_mock.called
    assert not delete_user_mock.called


@mock.patch("cv_creator.routes.get_user_by_user_id")
@mock.patch("cv_creator.routes.add_user")
@mock.patch("cv_creator.routes.update_user")
@mock.patch("cv_creator.routes.delete_user")
def test_delete_user_method_calls_with_decorators(delete_user_mock, update_user_mock, add_user_mock,
                                                  get_user_by_user_id_mock, client):
    user_id = 99
    response = client.delete(f"/user?user_id={user_id}")

    assert not get_user_by_user_id_mock.called
    assert not add_user_mock.called
    assert not update_user_mock.called
    assert delete_user_mock.called
    assert delete_user_mock.call_args == call(user_id)
    assert response.status_code == 200
    assert response.json["message"] == f'User with id {user_id} removed!'


def test_delete_user_method_calls(client):
    with mock.patch("cv_creator.routes.get_user_by_user_id") as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.delete("/user?user_id=99")

    assert not get_user_by_user_id_mock.called
    assert not add_user_mock.called
    assert not update_user_mock.called
    assert delete_user_mock.called
    assert delete_user_mock.call_args == call(99)


def test_get_user_values(client):
    first_name = "Seb"
    last_name = "Prz"
    permission = "admin"
    with mock.patch("cv_creator.routes.get_user_by_user_id") as get_user_by_user_id_mock:
        get_user_by_user_id_mock.return_value = User(
            first_name=first_name, last_name=last_name, permission=permission)
        response = client.get("/user?user_id=99")

    assert response.status_code == 200
    assert response.json["first_name"] == first_name
    assert response.json["last_name"] == last_name
    assert "permission" not in response.json


def test_add_user_controller(client):
    user = mock.create_autospec(User)
    user_db = mock.create_autospec(UserDb)
    user_db.id = 17
    user_db.first_name = 'seb'
    user_db.last_name = 'prz'
    user_db.permission = 'admin'

    with mock.patch('cv_creator.controllers.user_controller.repository.add_user', return_value=user_db):
        new_user = add_user(user)

    assert new_user.id == user_db.id
    assert new_user.first_name == user_db.first_name
    assert new_user.last_name == user_db.last_name
    assert new_user.permission == user_db.permission


def test_update_user_none(client):
    user_id = "99"
    with mock.patch("cv_creator.routes.get_user_by_user_id") as get_user_by_user_id_mock:
        get_user_by_user_id_mock.return_value = None
        response = client.patch("/user?user_id=%s" % user_id)

    assert response.status_code == 404
    assert response.json["message"] == ("User with id %s not found!" % user_id)


def test_update_user_controller(client):
    existing_user = User(id=15, first_name='seba', last_name='prze', permission='user')
    patch_user = UpdateUser(first_name='seb', last_name='prz', permission='admin')

    with mock.patch('cv_creator.controllers.user_controller.repository.update_user', return_value=patch_user):
        patched_user_db = update_user(existing_user.id, patch_user)

    assert patched_user_db.first_name == patch_user.first_name
    assert patched_user_db.last_name == patch_user.last_name
    assert patched_user_db.permission == patch_user.permission


def test_update_user_controller_one_field(client):
    existing_user = User(id=15, first_name='seba', last_name='prze', permission='user')
    patch_user = UpdateUser(last_name='prz')

    with mock.patch('cv_creator.controllers.user_controller.repository.update_user', return_value=patch_user):
        patched_user_db = update_user(existing_user.id, patch_user)

    assert patched_user_db.first_name == patch_user.first_name
    assert patched_user_db.last_name == patch_user.last_name
    assert patched_user_db.permission == patch_user.permission


def test_delete_user_controller_none(client):
    user_id = mock.create_autospec(int)

    with mock.patch('cv_creator.controllers.user_controller.repository.get_user_by_user_id', return_value=None):
        with mock.patch('cv_creator.controllers.user_controller.repository.delete_user') as mock_delete_user:
            delete_user(user_id)

    assert not mock_delete_user.called


def test_delete_user_controller(client):
    user_db = mock.create_autospec(UserDb)
    user_id = mock.create_autospec(int)

    with mock.patch('cv_creator.controllers.user_controller.repository.get_user_by_user_id', return_value=user_db):
        with mock.patch('cv_creator.controllers.user_controller.repository.delete_user') as mock_delete_user:
            delete_user(user_id)

    assert mock_delete_user.called


def test_get_user_controller_none(client):
    user_id = mock.create_autospec(int)

    with mock.patch('cv_creator.controllers.user_controller.repository.get_user_by_user_id', return_value=None):
        user = get_user_by_user_id(user_id)

    assert user is None


def test_get_user_controller(client):
    user_db = mock.create_autospec(UserDb)
    user_db.first_name = 'Rob'
    user_db.last_name = 'Son'
    user_id = mock.create_autospec(int)

    with mock.patch('cv_creator.controllers.user_controller.repository.get_user_by_user_id', return_value=user_db):
        user_from_db = get_user_by_user_id(user_id)

    assert user_db.first_name == user_from_db.first_name
    assert user_db.last_name == user_from_db.last_name
