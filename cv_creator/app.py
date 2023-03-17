from typing import Any

from flasgger import Swagger
from flask import Flask, jsonify, Response
from marshmallow import ValidationError

from cv_creator.routes import cv_creator


def create_app() -> Flask:
    app = Flask(__name__)
    swagger = Swagger(app)
    app.register_blueprint(cv_creator)
    app.register_error_handler(ValidationError, validation_handler)
    app.register_error_handler(404, page_not_found_handler)
    app.register_error_handler(500, server_error_handler)
    app.register_error_handler(KeyError, key_error_handler)
    return app


def validation_handler(e: Any) -> tuple[Response, int]:
    return jsonify({'message': e.messages}), 422


def page_not_found_handler() -> tuple[Response, int]:
    return jsonify({'message': 'Better luck next time!'}), 404


def server_error_handler() -> tuple[Response, int]:
    return jsonify({'error': 'An internal server error occurred'}), 500


def key_error_handler(e: Any) -> tuple[Response, int]:
    return jsonify({'error': f'Missing field in request body: {e}'}), 422


if __name__ == '__main__':
    create_app().run(debug=True)  # TODO get this from env
