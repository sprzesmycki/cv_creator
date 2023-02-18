from flask import request, make_response, Blueprint, jsonify

from cv_creator.schema.db_schema.db_serializers import user_db_schema, user_db_schema_without_id_and_permission
from .controllers.user_controller import get_user_by_user_id, add_user, update_user, delete_user
from .models.models import User
from .schema.api_schema.api_serializers import UserSchema

cv_creator = Blueprint('cv_creator', __name__)


@cv_creator.route('/user', methods=["GET"])
def get_user_request():
    """
    Get user by user_id
    ---
    parameters:
          - name: userId
            in: query
            type: integer
            required: true
    responses:
        200:
            description: User
        404:
            description: User not found
    """
    try:
        user_id: int = int(request.args.get('user_id'))
    except ValueError:
        return make_response(
            jsonify({'error': 'user_id is not an integer'}),
            400
        )
    user: User = get_user_by_user_id(user_id)
    return make_response(
        user_db_schema_without_id_and_permission.dump(user),
        200
    )


@cv_creator.route('/user', methods=["POST"])
def post_user_request():
    """
    Post user
    ---
    parameters:
            - name: user
              in: body
    responses:
        201:
            description: User created successfully
    """
    post_user: User = UserSchema.from_json(request.json)
    user: User = add_user(post_user)
    return make_response(
        user_db_schema.dump(user),
        201
    )


@cv_creator.route('/user', methods=["PATCH"])
def patch_user_request():
    """
    Patch user by user_id
    ---
    parameters:
          - name: user_id
            in: query
            type: integer
            required: true
          - name: user
            in: body
    responses:
        200:
            description: User
        404:
            description: User not found
    """
    user_id = int(request.args.get('user_id'))
    existing_user: User = get_user_by_user_id(user_id)
    if existing_user is None:
        return make_response(
            jsonify({'message': f'User with id {user_id} not found!'}),
            404
        )
    patch_user: User = UserSchema.from_json(request.json)
    user: User = update_user(existing_user, patch_user)
    return make_response(
        user_db_schema.dump(user),
        200
    )


@cv_creator.route('/user', methods=["DELETE"])
def delete_user_request():
    """
    Delete user by user_id
    ---
    parameters:
          - name: user_id
            in: query
            type: integer
            required: true
    responses:
        204:
            description: User deleted successfully
    """
    try:
        user_id: int = int(request.args.get('user_id'))
    except ValueError:
        return make_response(
            jsonify({'error': 'user_id is not an integer'}),
            400
        )
    delete_user(user_id)
    return make_response(
        jsonify({'message': f'User with id {user_id} removed!'}),  # for some reason this isn't displayed
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
        200
    )


@cv_creator.route('/stats', methods=["GET"])
def get_stats():
    return make_response(
        200
    )
