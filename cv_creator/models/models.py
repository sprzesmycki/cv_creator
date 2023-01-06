from dataclasses import field
from datetime import datetime
from typing import List, Optional

from marshmallow_dataclass import dataclass


@dataclass
class Skills:
    skill_name: str
    skill_id: Optional[int] = None

    @staticmethod
    def from_json(data):
        return Skills(
            skill_name=data['skill_name'],
            skill_id=data['skill_id'],
        )


@dataclass
class Company:
    company_name: str
    company_id: Optional[int] = None

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
    skill: Skills
    skill_level: int

    @staticmethod
    def from_json(data):
        return UserSkills(
            skill=Skills.from_json(data['skill']),
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
