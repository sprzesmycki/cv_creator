from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../cv_creator.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    permission = Column(String, nullable=False)  # todo probably replace with another class

    user_skills = relationship("UserSkills", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"


class Skills(db.Model):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill_name = Column(String, nullable=False, unique=True)

    user_skills = relationship("UserSkills", back_populates="skills")

    def __repr__(self):
        return f"Skills(id={self.id!r}, skill_name={self.skill_name!r}"


class UserSkills(db.Model):
    __tablename__ = 'user_skills'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)
    skill_level = Column(Integer, nullable=False)

    user = relationship("User", back_populates="user_skills")
    skills = relationship("Skills", back_populates="user_skills")

    def __repr__(self):
        return f"UserSkills(id={self.id!r}, user_id={self.user_id!r}, " \
               f"skill_id={self.skill_id!r}, skill_level={self.skill_level!r}) "
