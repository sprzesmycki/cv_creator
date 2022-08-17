from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../cv_creator.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    permission = db.Column(db.String, nullable=False)  # todo probably replace with another class

    user_skills = db.relationship('UserSkills', backref='user')
    user_experience = db.relationship('UserExperience', backref='user')

    def __repr__(self):
        return f'User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})'


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String, nullable=False, unique=True)

    user_skills = db.relationship('UserSkills', backref='skills')

    def __repr__(self):
        return f'Skills(id={self.id!r}, skill_name={self.skill_name!r}'


class UserSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)
    skill_level = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'UserSkills(id={self.id!r}, user_id={self.user_id!r}, ' \
               f'skill_id={self.skill_id!r}, skill_level={self.skill_level!r}) '


class UserExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_name = db.Column(db.String, nullable=False)
    job_description = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)  # todo datetime or just int
    end_date = db.Column(db.DateTime, nullable=False)  # todo datetime or just int

    def __repr__(self):
        return f'UserExperience(id={self.id!r}, user_id={self.user_id!r}, ' \
               f'company_name={self.company_name!r}, job_description={self.job_description!r}), ' \
               f'start_date={self.start_date!r}, end_date={self.end_date!r}) '


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
