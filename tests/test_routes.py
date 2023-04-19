import random

import mock
from mock import call

from cv_creator.models.models import User


def test_get_user_method_calls(client):
    with mock.patch(
        "cv_creator.routes.get_user_by_user_id"
    ) as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.get("/user?id=99")

    assert get_user_by_user_id_mock.called
    assert get_user_by_user_id_mock.call_args == call(99)
    assert not add_user_mock.called
    assert not update_user_mock.called
    assert not delete_user_mock.called


def test_post_user_method_calls(client):
    with mock.patch(
        "cv_creator.routes.get_user_by_user_id"
    ) as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.post(
                        "/user",
                        json={
                            "first_name": "seb",
                            "last_name": "as",
                            "permission": "admin",
                        },
                    )

    assert add_user_mock.called
    assert not get_user_by_user_id_mock.called
    assert not update_user_mock.called
    assert not delete_user_mock.called


def test_patch_user_method_calls(client):
    with mock.patch(
        "cv_creator.routes.get_user_by_user_id"
    ) as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.patch(
                        "/user?id=99",
                        json={
                            "first_name": "huhhfffdfgfgfue",
                            "id": "22",
                            "last_name": "sebzodfdfnek",
                        },
                    )

    assert not add_user_mock.called
    assert get_user_by_user_id_mock.called
    assert update_user_mock.called
    assert not delete_user_mock.called


@mock.patch("cv_creator.routes.get_user_by_user_id")
@mock.patch("cv_creator.routes.add_user")
@mock.patch("cv_creator.routes.update_user")
@mock.patch("cv_creator.routes.delete_user")
def test_delete_user_method_calls_with_decorators(
    delete_user_mock, update_user_mock, add_user_mock, get_user_by_user_id_mock, client
):
    user_id = 99
    response = client.delete(f"/user?id={user_id}")

    assert not get_user_by_user_id_mock.called
    assert not add_user_mock.called
    assert not update_user_mock.called
    assert delete_user_mock.called
    assert delete_user_mock.call_args == call(user_id)
    assert response.status_code == 200
    assert response.json["message"] == f"User with id {user_id} removed!"


def test_delete_user_method_calls(client):
    with mock.patch(
        "cv_creator.routes.get_user_by_user_id"
    ) as get_user_by_user_id_mock:
        with mock.patch("cv_creator.routes.add_user") as add_user_mock:
            with mock.patch("cv_creator.routes.update_user") as update_user_mock:
                with mock.patch("cv_creator.routes.delete_user") as delete_user_mock:
                    client.delete("/user?id=99")

    assert not get_user_by_user_id_mock.called
    assert not add_user_mock.called
    assert not update_user_mock.called
    assert delete_user_mock.called
    assert delete_user_mock.call_args == call(99)


def test_get_user_values(client):
    first_name = "Seb"
    last_name = "Prz"
    permission = "admin"
    with mock.patch(
        "cv_creator.routes.get_user_by_user_id"
    ) as get_user_by_user_id_mock:
        get_user_by_user_id_mock.return_value = User(
            first_name=first_name, last_name=last_name, permission=permission
        )
        response = client.get("/user?id=99")

    assert response.status_code == 200
    assert response.json["first_name"] == first_name
    assert response.json["last_name"] == last_name
    assert "permission" not in response.json


def test_update_user_none(client):
    user_id = "99"
    with mock.patch(
        "cv_creator.routes.get_user_by_user_id"
    ) as get_user_by_user_id_mock:
        get_user_by_user_id_mock.return_value = None
        response = client.patch("/user?id=%s" % user_id)

    assert response.status_code == 404
    assert response.json["message"] == ("User with id %s not found!" % user_id)


@mock.patch("cv_creator.routes.get_users_count_with_skill")
def test_get_users_with_skill_count(get_users_count_with_skill_mock, client):
    skill_id = 99
    skill_level = random.randint(1, 5)
    count = random.randint(1, 50)
    get_users_count_with_skill_mock.return_value = count
    response = client.get(f"/stats?skill_id={skill_id}&skill_level={skill_level}")

    assert get_users_count_with_skill_mock.call_args == call(skill_id, skill_level)
    assert response.status_code == 200
    assert response.json["count"] == str(count)
