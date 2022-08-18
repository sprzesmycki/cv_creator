from flask import json, request, make_response, Blueprint

from flaskapp import models
from flaskapp.database import SessionLocal, engine
from flaskapp.serializers import UserSchema

cv_creator = Blueprint('cv_creator', __name__)

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)


@cv_creator.route('/user', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def user():
    user_schema = UserSchema()
    if request.method == 'GET':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'POST':
        data = json.loads(request.data)  # todo probably context-type validation required and handling missing fields
        user_details = models.User(first_name=data['first_name'], last_name=data['last_name'],
                                   permission=data['permission'])
        db.add(user_details)
        db.commit()
        return make_response(
            user_schema.dump(user_details),
            200
        )
    if request.method == 'PUT':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'PATCH':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'DELETE':
        return make_response(
            "I will do that sometime later",
            418
        )


@cv_creator.route('/cv', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def cv():
    return "I will do that sometime later"


@cv_creator.route('/stats', methods=["GET"])  # todo should I user methods=["GET"] even if its default one?
def get_stats():
    return "I will do that sometime later"