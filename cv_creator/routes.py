import json

from flask import request, make_response, Blueprint

from .controllers.user_controller import get_user_by_user_id, add_user, update_user, delete_user
from .serializers.db_serializers import GetUserSchema, CompleteUserSchema, PostUserSchema

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET", "POST", "PATCH", "DELETE"])
def user_requests():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        user = get_user_by_user_id(user_id)
        get_user_schema = GetUserSchema()
        return make_response(
            get_user_schema.dump(user),
            200
        )
    if request.method == 'POST':
        user_payload = json.dumps(request.json)
        post_user = PostUserSchema().load(user_payload)
        new_user = add_user(post_user)
        complete_user_schema = CompleteUserSchema()
        return make_response(
            complete_user_schema.dump(new_user),
            201
        )
    if request.method == 'PATCH':
        user_id = request.args.get('user_id')
        post_user_schema = PostUserSchema()
        post_user = post_user_schema.dump(request.json)
        user = update_user(user_id, post_user)
        complete_user_schema = CompleteUserSchema()
        return make_response(
            complete_user_schema.dump(user),
            200
        )
    if request.method == 'DELETE':
        user_id = request.args.get('user_id')
        delete_user(user_id)
        return make_response(
            '',
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
def experience_requests():
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
