import marshmallow

from cv_creator.app import validation_handler_marshmallow


def test_page_not_found_handler(client):
    response = client.get('/fake-endpoint')
    assert response.status_code == 404
    assert response.get_json() == {'message': 'Better luck next time!'}


def test_validation_handler_marshmallow(client):
    with client.application.app_context():
        mock_error = marshmallow.ValidationError(message='Invalid input')
        response, status_code = validation_handler_marshmallow(mock_error)

        assert status_code == 422
        assert response.get_json() == {'message': ['Invalid input']}
