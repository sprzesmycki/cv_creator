from flask import request, make_response, Blueprint, jsonify

from .controllers.user_controller import get_user_by_user_id, add_user, update_user, delete_user
from .models.models import User
from .serializers.db_serializers import GetUserSchema, CompleteUserSchema, PostUserSchema

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET", "POST", "PATCH", "DELETE"])
def user_requests():
    match request.method:
        case 'GET':
            user_id = request.args.get('userId')
            user: User = get_user_by_user_id(user_id)
            return make_response(
                GetUserSchema().dump(user),
                200
            )
        case 'POST':
            post_user = User.Schema().load(request.json)
            new_user: User = add_user(post_user)
            return make_response(
                CompleteUserSchema().dump(new_user),
                201
            )
        case 'PATCH':
            user_id = request.args.get('userId')
            post_user = PostUserSchema().dump(request.json)
            user: User = update_user(user_id, post_user)
            return make_response(
                CompleteUserSchema().dump(user),
                200
            )
        case 'DELETE':
            user_id = request.args.get('userId')
            delete_user(user_id)
            return jsonify({'message': f'User with id {user_id} removed!'}), 204


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
