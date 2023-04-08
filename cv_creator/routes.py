from typing import Optional

from flasgger import swag_from
from flask import request, make_response, Blueprint, jsonify, Response

from cv_creator.schema.db_schema.db_serializers import (
    user_db_schema,
    user_db_schema_without_id_and_permission,
)
from .controllers.stats_controller import get_users_count_with_skill
from .controllers.user_controller import (
    get_user_by_user_id,
    add_user,
    update_user,
    delete_user,
)
from .models.models import User, UpdateUser
from .schema.api_schema.api_serializers import (
    UserSchema,
    UpdateUserSchema,
    UserArgsSchema,
    StatsArgsSchema,
)

cv_creator = Blueprint("cv_creator", __name__)


@cv_creator.route("/user", methods=["GET"])
@swag_from("doc/get_user.yml")
def get_user_request() -> Response:
    validated_args = UserArgsSchema.parse_obj(request.args)
    user: Optional[User] = get_user_by_user_id(validated_args.user_id)
    return make_response(user_db_schema_without_id_and_permission.dump(user), 200)


@cv_creator.route("/user", methods=["POST"])
@swag_from("doc/post_user.yml")
def post_user_request() -> Response:
    validated_user = UserSchema.parse_obj(request.json)
    post_user: User = User(**dict(validated_user))
    user: User = add_user(post_user)
    return make_response(user_db_schema.dump(user), 201)


@cv_creator.route("/user", methods=["PATCH"])
@swag_from("doc/patch_user.yml")
def patch_user_request() -> Response:
    args = request.args.to_dict()
    validated_args = UserArgsSchema(**args)
    existing_user: User = get_user_by_user_id(validated_args.user_id)
    if existing_user is None:
        return make_response(
            jsonify({"message": f"User with id {validated_args.user_id} not found!"}),
            404,
        )
    validated_user = UpdateUserSchema.parse_obj(request.json)
    patch_user: Optional[UpdateUser] = UpdateUser(**dict(validated_user))
    if patch_user is None:
        return make_response(jsonify({"message": "No data to update!"}), 400)
    user: User = update_user(validated_args.user_id, patch_user)
    return make_response(user_db_schema.dump(user), 200)


@cv_creator.route("/user", methods=["DELETE"])
@swag_from("doc/delete_user.yml")
def delete_user_request() -> Response:
    args = request.args.to_dict()
    validated_args = UserArgsSchema(**args)
    delete_user(validated_args.user_id)
    return make_response(
        jsonify({"message": f"User with id {validated_args.user_id} removed!"}), 200
    )


@cv_creator.route("/user/skills", methods=["GET", "POST", "PATCH", "DELETE"])
def skill_requests() -> Response:
    if request.method == "GET":
        return make_response(200)
    if request.method == "POST":
        return make_response(201)
    if request.method == "PATCH":
        return make_response(200)
    if request.method == "DELETE":
        return make_response(204)


@cv_creator.route("/user/experience", methods=["GET", "POST", "PATCH", "DELETE"])
def experience_requests() -> Response:
    if request.method == "GET":
        return make_response(200)
    if request.method == "POST":
        return make_response(201)
    if request.method == "PATCH":
        return make_response(200)
    if request.method == "DELETE":
        return make_response(204)


@cv_creator.route("/cv", methods=["GET"])
def cv_requests() -> Response:
    return make_response(200)


@cv_creator.route("/stats", methods=["GET"])
@swag_from("doc/get_stats.yml")
def get_stats() -> Response:
    validated_args = StatsArgsSchema.parse_obj(request.args)
    count: int = get_users_count_with_skill(
        validated_args.skill_id, validated_args.skill_level
    )
    return make_response(jsonify({"count": f"{count}"}), 200)
