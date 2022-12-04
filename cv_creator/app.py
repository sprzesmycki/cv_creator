from flask import Flask
from marshmallow import ValidationError

from cv_creator.routes import cv_creator


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cv_creator)
    app.register_error_handler(ValidationError, validation_handler)
    app.register_error_handler(404, page_not_found_handler)
    app.register_error_handler(500, server_error_handler)
    return app


def validation_handler(e):
    return e.messages, 422


def page_not_found_handler(e):
    return 'Better luck next time!', 200  # todo not sure what to do in handlers


def server_error_handler(e):
    return e, 500  # todo not sure what to do in handlers


if __name__ == '__main__':
    create_app().run()
