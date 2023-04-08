import marshmallow

from cv_creator.app import validation_handler_marshmallow, server_error_handler


def test_page_not_found_handler(client):
    response = client.get("/fake-endpoint")
    assert response.status_code == 404
    assert response.get_json() == {"message": "Better luck next time!"}


def test_validation_handler_marshmallow(client):
    with client.application.app_context():
        mock_error = marshmallow.ValidationError(message="Invalid input")
        response, status_code = validation_handler_marshmallow(mock_error)

        assert status_code == 500
        assert response.get_json() == {"details": ["Invalid input"]}


def test_validation_handler_pydantic(client):
    response = client.post(
        "/user",
        json={
            "first_name": "Sebastian",
            "last_name": "Przybylski",
            "permission": "admin",
            "email": "",
        },
    )
    assert response.status_code == 422
    assert response.get_json() == {
        "details": [
            {
                "loc": ["user_experience"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["user_skills"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["email"],
                "msg": "extra fields not permitted",
                "type": "value_error.extra",
            },
        ]
    }


def test_server_error_handler(client):
    with client.application.app_context():
        mock_error = SystemError("Internal server error")
        response, status_code = server_error_handler(mock_error)

        assert status_code == 500
        assert response.get_json() == {"error": "An internal server error occurred"}
