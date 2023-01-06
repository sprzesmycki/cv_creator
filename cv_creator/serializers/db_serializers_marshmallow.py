import marshmallow


class UserExperienceSerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    user_id = marshmallow.fields.Int(required=True)
    company_id = marshmallow.fields.Int(required=True)
    job_description = marshmallow.fields.Str(required=True)
    start_date = marshmallow.fields.DateTime(required=True)
    end_date = marshmallow.fields.DateTime(required=True)


class UserSkillsSerializer(marshmallow.Schema):
    user_id = marshmallow.fields.Int(required=True)
    skill_id = marshmallow.fields.Int(required=True)
    skill_level = marshmallow.fields.Int(required=True)


class UserSerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    first_name = marshmallow.fields.Str(required=True)
    last_name = marshmallow.fields.Str(required=True)
    permission = marshmallow.fields.Str(required=True)
    user_skills = marshmallow.fields.Nested(UserSkillsSerializer, many=True)
    user_experience = marshmallow.fields.Nested(UserExperienceSerializer, many=True)


class SkillsSerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    skill_name = marshmallow.fields.Str(required=True)


class CompanySerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    company_name = marshmallow.fields.Str(required=True)


user_experience_schema = UserExperienceSerializer()
user_skills_schema = UserSkillsSerializer()
user_schema = UserSerializer()
skills_schema = SkillsSerializer()
company_schema = CompanySerializer()
