from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from flaskapp.models import User, UserSkills, UserExperience, Skills, Company


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    id = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    permission = auto_field()
    user_skills = auto_field()
    user_experience = auto_field()


class SkillsSchema(SQLAlchemySchema):
    class Meta:
        model = Skills
        include_relationships = True
        load_instance = True


class UserSkillsSchema(SQLAlchemySchema):
    class Meta:
        model = UserSkills
        include_relationships = True
        load_instance = True


class UserExperienceSchema(SQLAlchemySchema):
    class Meta:
        model = UserExperience
        include_relationships = True
        load_instance = True


class CompanySchema(SQLAlchemySchema):
    class Meta:
        model = Company
        include_relationships = True
        load_instance = True
