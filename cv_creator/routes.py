from flask import request, make_response, Blueprint

from .models.models import User
from .serializers.db_serializers import GetUserSchema, PostUserSchema
from .controllers.user_controller import get_user_by_user_id, add_user, update_user, delete_user

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET", "POST", "PATCH", "DELETE"])
def user_requests():
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
        user_id = request.args.get('userId')
        return make_response(
            delete_user(user_id),  # makes no sense to call it there due to fact that 204 is not returning value
            204
        )


@cv_creator.route('/user/skills', methods=["GET", "POST", "PATCH", "DELETE"])
def skill_requests():
    if request.method == 'GET':
        return make_response(
            200
        )
    if request.method == 'POST':
        return make_response(
            201
        )
    if request.method == 'PATCH':
        return make_response(
            200
        )
    if request.method == 'DELETE':
        return make_response(
            204
        )


@cv_creator.route('/user/experience', methods=["GET", "POST", "PATCH", "DELETE"])
def skill_requests():
    if request.method == 'GET':
        return make_response(
            200
        )
    if request.method == 'POST':
        return make_response(
            201
        )
    if request.method == 'PATCH':
        return make_response(
            200
        )
    if request.method == 'DELETE':
        return make_response(
            204
        )


@cv_creator.route('/cv', methods=["GET"])
def cv_requests():
    return make_response(
        # get_cv(cv_id)
        200
    )


@cv_creator.route('/stats', methods=["GET"])
def get_stats():
    return make_response(
        200
    )
