from marshmallow import post_load
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from cv_creator.storage.postgres.db_models import UserDb, UserSkillsDb, UserExperienceDb, SkillsDb, CompanyDb


class CompleteUserSchema(SQLAlchemySchema):
    class Meta:
        model = UserDb
        include_relationships = True
        load_instance = True

    id = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    permission = auto_field()
    user_skills = auto_field()
    user_experience = auto_field()

    @post_load
    def make_user(self, data, **kwargs):
        return UserDb(**data)


class PostUserSchema(SQLAlchemySchema):
    class Meta:
        model = UserDb
        include_relationships = True
        load_instance = True

    first_name = auto_field()
    last_name = auto_field()
    permission = auto_field()
    user_skills = auto_field()
    user_experience = auto_field()


class GetUserSchema(SQLAlchemySchema):
    class Meta:
        model = UserDb
        include_relationships = True
        load_instance = True

    first_name = auto_field()
    last_name = auto_field()
    user_skills = auto_field()
    user_experience = auto_field()


class SkillsDbSchema(SQLAlchemySchema):
    class Meta:
        model = SkillsDb
        include_relationships = True
        load_instance = True


class UserSkillsDbSchema(SQLAlchemySchema):
    class Meta:
        model = UserSkillsDb
        include_relationships = True
        load_instance = True


class UserExperienceDbSchema(SQLAlchemySchema):
    class Meta:
        model = UserExperienceDb
        include_relationships = True
        load_instance = True


class CompanyDbSchema(SQLAlchemySchema):
    class Meta:
        model = CompanyDb
        include_relationships = True
        load_instance = True
