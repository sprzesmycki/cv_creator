from flask_marshmallow import Marshmallow

from flaskapp.app import app
from flaskapp.database import User, UserSkills, UserExperience

ma = Marshmallow(app)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


class UserSkillsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserSkills
        include_relationships = True
        load_instance = True


class UserExperienceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserExperience
        include_relationships = True
        load_instance = True
