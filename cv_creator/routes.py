from flask import request, make_response, Blueprint, jsonify

from .controllers.user_controller import get_user_by_user_id, add_user, update_user, delete_user
from .models.models import User
from .serializers.db_serializers import user_db_schema, user_db_schema_without_id_and_permission

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET", "POST", "PATCH", "DELETE"])
def user_requests():
    match request.method:
        case 'GET':
            user_id = int(request.args.get('userId'))
            user: User = get_user_by_user_id(user_id)
            return make_response(
                user_db_schema_without_id_and_permission.dump(user),
                200
            )
        case 'POST':
            post_user: User = User.from_json(request.json)
            user: User = add_user(post_user)
            return make_response(
                user_db_schema.dump(user),
                201
            )
        case 'PATCH':
            user_id = int(request.args.get('userId'))
            existing_user: User = get_user_by_user_id(user_id)
            if existing_user is None:
                return make_response(
                    jsonify({'message': f'User with id {user_id} not found!'}),
                    404
                )
            user_patch: User = User.from_json(request.json)
            user: User = update_user(existing_user, user_patch)
            return make_response(
                user_db_schema.dump(user),
                200
            )
        case 'DELETE':
            user_id = int(request.args.get('userId'))
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
        200
    )


@cv_creator.route('/stats', methods=["GET"])
def get_stats():
    return make_response(
        200
    )
