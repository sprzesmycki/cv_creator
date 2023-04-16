import marshmallow


class DbUserExperienceSerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    user_id = marshmallow.fields.Int(required=True)
    company_id = marshmallow.fields.Int(required=True)
    job_description = marshmallow.fields.Str(required=True)
    start_date = marshmallow.fields.DateTime(required=True)
    end_date = marshmallow.fields.DateTime(required=True)


class DbUserSkillsSerializer(marshmallow.Schema):
    user_id = marshmallow.fields.Int(required=True)
    skill_id = marshmallow.fields.Int(required=True)
    skill_level = marshmallow.fields.Int(required=True)


class DbUserSerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    first_name = marshmallow.fields.Str(required=True)
    last_name = marshmallow.fields.Str(required=True)
    permission = marshmallow.fields.Str(required=True)
    user_skills = marshmallow.fields.Nested(DbUserSkillsSerializer, many=True)
    user_experience = marshmallow.fields.Nested(DbUserExperienceSerializer, many=True)


class DbSkillSerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    skill_name = marshmallow.fields.Str(required=True)


class DbCompanySerializer(marshmallow.Schema):
    id = marshmallow.fields.Int(required=True)
    company_name = marshmallow.fields.Str(required=True)


user_db_schema_without_id = DbUserSerializer(exclude=("id",))
user_db_schema_without_id_and_permission = DbUserSerializer(
    exclude=("id", "permission")
)
user_experience_db_schema = DbUserExperienceSerializer()
user_skills_db_schema = DbUserSkillsSerializer()
user_db_schema = DbUserSerializer()
skill_db_schema = DbSkillSerializer()
company_db_schema = DbCompanySerializer()
