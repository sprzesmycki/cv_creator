from flask import Flask
from .routes import cv_creator

app = Flask(__name__)
app.register_blueprint(cv_creator)


if __name__ == '__main__':
    app.run()
