from flask import Flask
from marshmallow import ValidationError

from cv_creator.routes import cv_creator


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cv_creator)
    app.register_error_handler(ValidationError, validation_handler)
    return app


def validation_handler(e):
    return e.messages, 422


if __name__ == '__main__':
    create_app().run()
