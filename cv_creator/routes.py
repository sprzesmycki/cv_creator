from flask import request, make_response, Blueprint

from .models.models import User
from .serializers.db_serializers import GetUserSchema, PostUserSchema
from .controllers.user_controller import get_user_by_user_id, add_user, update_user

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def user_request():
    if request.method == 'GET':
        get_user_schema = GetUserSchema()
        user_id = request.args.get('userId')
        return make_response(
            get_user_schema.dump(get_user_by_user_id(user_id)),
            200
        )
    if request.method == 'POST':
        user = User(
            first_name=request.json['first_name'],
            last_name=request.json['last_name'],
            permission=request.json['permission']
        )
        post_user_schema = PostUserSchema()
        return make_response(
            post_user_schema.dump(add_user(user)),
            201
        )
    if request.method == 'PUT':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'PATCH':
        user = User(
            id=request.json['id'],
            first_name=request.json['first_name'],
            last_name=request.json['last_name'],
            permission=request.json['permission'],
            user_skills=request.json['user_skills'],
            user_experience=request.json['user_experience']
        )
        post_user_schema = PostUserSchema()
        return make_response(
            post_user_schema.dump(update_user(user)),
            200
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
