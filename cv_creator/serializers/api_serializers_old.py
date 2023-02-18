from marshmallow import Schema, post_load, fields

from cv_creator.models.models import User


class SkillSchema(Schema):
    skill_name = fields.Str()
    skill_id = fields.Int()


class UserSkillsSchema(Schema):
    skill = fields.Nested(SkillSchema())
    skill_level = fields.Int()


class CompanySchema(Schema):
    company_name = fields.Str()
    company_id = fields.Str()


class UserExperienceSchema(Schema):
    company = fields.Nested(CompanySchema())
    job_description = fields.Str()
    start_date: fields.DateTime
    end_date: fields.DateTime


class UserSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    permission = fields.Str()
    user_skills = fields.List(fields.Nested(UserSkillsSchema()), required=False)
    user_experience = fields.List(fields.Nested(UserExperienceSchema()), required=False)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
