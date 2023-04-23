import marshmallow
import pydantic
from flasgger import Swagger
from flask import Flask, jsonify, Response
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from cv_creator.routes import cv_creator


def create_app() -> Flask:
    app = Flask(__name__)
    swagger = Swagger(app)
    app.register_blueprint(cv_creator)
    app.register_error_handler(
        marshmallow.ValidationError, validation_handler_marshmallow
    )
    app.register_error_handler(pydantic.ValidationError, validation_handler_pydantic)
    app.register_error_handler(IntegrityError, integrity_error_handler)
    app.register_error_handler(ValueError, value_error_handler)
    app.register_error_handler(404, page_not_found_handler)
    app.register_error_handler(500, server_error_handler)
    return app


def validation_handler_marshmallow(
    e: marshmallow.ValidationError,
) -> tuple[Response, int]:
    return jsonify({"details": e.messages}), 500


def validation_handler_pydantic(e: pydantic.ValidationError) -> tuple[Response, int]:
    return jsonify({"details": e.errors()}), 422


def page_not_found_handler(e: NotFound) -> tuple[Response, int]:
    return jsonify({"message": "Better luck next time!"}), 404


def server_error_handler(e: SystemError) -> tuple[Response, int]:
    return jsonify({"error": "An internal server error occurred"}), 500


def integrity_error_handler(e: IntegrityError) -> tuple[Response, int]:
    return jsonify({"error": "Value already exists"}), 200


def value_error_handler(e: ValueError) -> tuple[Response, int]:
    return jsonify({"error": e.args}), 200


if __name__ == "__main__":
    create_app().run()
