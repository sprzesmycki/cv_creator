from flask import request, make_response, Blueprint

from .serializers import GetUserSchema, PostUserSchema
from .controllers.user_controller import get_user, add_user

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def user():
    if request.method == 'GET':
        get_user_schema = GetUserSchema()
        return make_response(
            get_user_schema.dump(get_user(request.args.get('userId'))),
            200
        )
    if request.method == 'POST':
        post_user_schema = PostUserSchema()
        return make_response(
            post_user_schema.dump(add_user(request)),
            201
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
