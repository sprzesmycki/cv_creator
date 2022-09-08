from dataclasses import field
from datetime import datetime
from typing import List

from marshmallow_dataclass import dataclass


@dataclass
class Skills:
    skill_name: str
    skill_id: int = None


@dataclass
class Company:
    company_name: str
    company_id: int = None


@dataclass
class UserExperience:
    company: Company
    job_description: str
    start_date: datetime
    end_date: datetime


@dataclass
class UserSkills:
    skill: Skills
    skill_level: int


@dataclass
class User:
    first_name: str
    last_name: str
    permission: str
    id: int = None
    user_skills: List[UserSkills] = field(default_factory=list)
    user_experience: List[UserExperience] = field(default_factory=list)
