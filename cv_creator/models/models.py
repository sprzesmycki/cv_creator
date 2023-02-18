from dataclasses import field
from datetime import datetime
from typing import List, Optional

from marshmallow_dataclass import dataclass


@dataclass
class Skill:
    skill_name: str
    skill_id: Optional[int] = None

    def __init__(self, skill_name, skill_id):
        self.skill_name = skill_name
        self.skill_id = skill_id

    @staticmethod
    def from_json(data):
        return Skill(
            skill_name=data['skill_name'],
            skill_id=data['skill_id'],
        )


@dataclass
class Company:
    company_name: str
    company_id: Optional[int] = None

    def __init__(self, company_name, company_id):
        self.company_name = company_name
        self.company_id = company_id

    @staticmethod
    def from_json(data):
        return Company(
            company_name=data['company_data'],
            company_id=data['company_id'],
        )


@dataclass
class UserExperience:
    company: Company
    job_description: str
    start_date: datetime
    end_date: datetime

    def __init__(self, company, job_description, start_date, end_date):
        self.company = company
        self.job_description = job_description
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def from_json(data):
        return UserExperience(
            company=Company.from_json(data['company']),
            job_description=data['job_description'],
            start_date=data['start_date'],
            end_date=data['end_date'],
        )


@dataclass
class UserSkills:
    skill: Skill
    skill_level: int

    def __init__(self, skill, skill_level):
        self.skill = skill
        self.skill_level = skill_level

    @staticmethod
    def from_json(data):
        return UserSkills(
            skill=Skill.from_json(data['skill']),
            skill_level=data['skill_level'],
        )


@dataclass
class User:
    first_name: str
    last_name: str
    permission: str
    id: Optional[int] = field(default=None, repr=False)
    user_skills: List[UserSkills] = field(default_factory=list)
    user_experience: List[UserExperience] = field(default_factory=list)

    def __init__(self, first_name, last_name, permission, id=None, user_skills=None, user_experience=None):
        self.first_name = first_name
        self.last_name = last_name
        self.permission = permission
        self.id = id
        self.user_skills = user_skills
        self.user_experience = user_experience

    @staticmethod
    def from_json(data):
        return User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            permission=data['permission'],
            id=data.get('id'),
            user_skills=[UserSkills.from_json(skills) for skills in data['user_skills']],
            user_experience=[UserExperience.from_json(experience) for experience in data['user_experience']],
        )
