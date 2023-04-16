from typing import Optional

from flasgger import swag_from
from flask import request, make_response, Blueprint, jsonify, Response

from cv_creator.schema.db_schema.db_serializers import (
    user_db_schema,
    user_db_schema_without_id_and_permission,
    skill_db_schema,
    user_experience_db_schema,
)
from .controllers.skill_controller import get_skill_by_skill_id, add_skill, delete_skill
from .controllers.stats_controller import get_users_count_with_skill
from .controllers.user_controller import (
    get_user_by_user_id,
    add_user,
    update_user,
    delete_user,
    get_user_experience_by_user_id,
    add_user_experience,
    get_user_experience_by_user_experience_id,
    update_user_experience,
)
from .models.models import User, UpdateUser, Skill, UserExperience
from .schema.api_schema.api_serializers import (
    UserSchema,
    UpdateUserSchema,
    UserArgsSchema,
    StatsArgsSchema,
    SkillArgsSchema,
    SkillSchema,
    UserExperienceSchema,
    UpdateUserExperienceSchema,
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
    validated_args = UserArgsSchema.parse_obj(request.args)
    existing_user: Optional[User] = get_user_by_user_id(validated_args.user_id)
    if existing_user is None:
        return make_response(
            jsonify({"message": f"User with id {validated_args.user_id} not found!"}),
            404,
        )
    validated_user = UpdateUserSchema.parse_obj(request.json)
    patch_user: Optional[UpdateUser] = UpdateUser(**dict(validated_user))
    if patch_user is None:
        return make_response(jsonify({"message": "No data to update!"}), 400)
    user: Optional[User] = update_user(validated_args.user_id, patch_user)
    return make_response(user_db_schema.dump(user), 200)


@cv_creator.route("/user", methods=["DELETE"])
@swag_from("doc/delete_user.yml")
def delete_user_request() -> Response:
    validated_args = UserArgsSchema.parse_obj(request.args)
    delete_user(validated_args.user_id)
    return make_response(
        jsonify({"message": f"User with id {validated_args.user_id} removed!"}), 200
    )


@cv_creator.route("/skill", methods=["GET"])
# @swag_from("doc/get_skill.yml")
def get_skill_request() -> Response:
    validated_args = SkillArgsSchema.parse_obj(request.args)
    skill: Optional[Skill] = get_skill_by_skill_id(validated_args.skill_id)
    return make_response(skill_db_schema.dump(skill), 200)


@cv_creator.route("/skill", methods=["POST"])
# @swag_from("doc/post_skill.yml")
def post_skill_request() -> Response:
    validated_skill = SkillSchema.parse_obj(request.json)
    post_skill: Skill = Skill(**dict(validated_skill))
    skill: Skill = add_skill(post_skill)
    return make_response(skill_db_schema.dump(skill), 201)


@cv_creator.route("/skill", methods=["DELETE"])
# @swag_from("doc/delete_skill.yml")
def delete_skill_request() -> Response:
    validated_args = SkillArgsSchema.parse_obj(request.args)
    delete_skill(validated_args.skill_id)
    return make_response(
        jsonify({"message": f"Skill with id {validated_args.skill_id} removed!"}), 200
    )


@cv_creator.route("/user/experience", methods=["GET"])
# @swag_from("doc/get_user_experience.yml")
def get_user_experience_request() -> Response:
    validated_args = UserArgsSchema.parse_obj(request.args)
    user: Optional[User] = get_user_by_user_id(validated_args.user_id)
    if user is None:
        return make_response(
            jsonify({"message": f"User with id {validated_args.user_id} not found!"}),
            404,
        )
    user_experience = get_user_experience_by_user_id(validated_args.user_id)
    return make_response(user_experience_db_schema.dump(user_experience), 200)


@cv_creator.route("/user/experience", methods=["POST"])
# @swag_from("doc/post_user_experience.yml")
def post_user_experience_request() -> Response:
    validated_args = UserArgsSchema.parse_obj(request.args)
    validated_user_experience = UserExperienceSchema.parse_obj(request.json)
    post_experience: UserExperience = UserExperience(**dict(validated_user_experience))
    user_experience: UserExperience = add_user_experience(
        validated_args.user_id, post_experience
    )
    return make_response(user_db_schema.dump(user_experience), 201)


@cv_creator.route("/user/experience", methods=["PATCH"])
# @swag_from("doc/patch_user_experience.yml")
def patch_user_experience_request() -> Response:
    validated_args = UserArgsSchema.parse_obj(request.args)
    existing_user: Optional[User] = get_user_by_user_id(validated_args.user_id)
    if existing_user is None:
        return make_response(
            jsonify({"message": f"User with id {validated_args.user_id} not found!"}),
            404,
        )
    validated_user_experience = UpdateUserExperienceSchema.parse_obj(request.json)
    user_experience: Optional[
        UserExperience
    ] = get_user_experience_by_user_experience_id(
        validated_user_experience.user_experience_id
    )
    if user_experience is None:
        return make_response(
            jsonify({"message": f"User experience not found!"}),
            404,
        )

    patch_user_experience: UserExperience = UserExperience(
        **dict(validated_user_experience)
    )
    updated_user_experience: Optional[UserExperience] = update_user_experience(
        validated_user_experience.user_experience_id, patch_user_experience
    )
    return make_response(user_experience_db_schema.dump(updated_user_experience), 200)


@cv_creator.route("/user/experience", methods=["DELETE"])
# @swag_from("doc/delete_user_experience.yml")
def delete_user_experience_request() -> Response:
    validated_args = UserArgsSchema.parse_obj(request.args)
    delete_user(validated_args.user_id)
    return make_response(
        jsonify({"message": f"User with id {validated_args.user_id} removed!"}), 200
    )


@cv_creator.route("/stats", methods=["GET"])
# @swag_from("doc/get_stats.yml")
def get_stats() -> Response:
    validated_args = StatsArgsSchema.parse_obj(request.args)
    count: int = get_users_count_with_skill(
        validated_args.skill_id, validated_args.skill_level
    )
    return make_response(jsonify({"count": f"{count}"}), 200)
