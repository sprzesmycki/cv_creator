import pytest
import requests
import requests_mock
from requests_mock_flask import add_flask_app_to_mock

from cv_creator.app import create_app


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


def test_request_get_user(client):
    response = client.get("/user?userId=1")
    assert response.status_code == 200
    assert b'{"first_name":"seb","last_name":"as","user_experience":[],"user_skills":[]}\n' in response.data


def test_request_post_user(client):
    first_name = "seb"
    last_name = "as"
    role = "admin"
    response = client.post("/user", json={
        "first_name": ("%s" % first_name),
        "last_name": ("%s" % last_name),
        "permission": ("%s" % role)
    })
    assert response.status_code == 201
    assert response.json["first_name"] == first_name
    assert response.json["last_name"] == last_name
    assert response.json["permission"] == role


def test_requests_mock_context_manager(app) -> None:
    with requests_mock.Mocker() as resp_m:
        add_flask_app_to_mock(
            mock_obj=resp_m,
            flask_app=app,
            base_url='http://127.0.0.1:5000/user?userId=1',
        )

        response = requests.get('http://127.0.0.1:5000/user?userId=1')

    assert response.status_code == 200
    assert response.text == 'Hello, World!'
