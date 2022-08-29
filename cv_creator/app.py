from flask import Flask
from cv_creator.routes import cv_creator


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cv_creator)
    return app


if __name__ == '__main__':
    create_app().run()
