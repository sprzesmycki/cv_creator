from dataclasses import dataclass, field
from datetime import datetime

from typing import List


@dataclass
class Skills:
    skill_id: int
    skill_name: str


@dataclass
class Company:
    company_id: int
    company_name: str


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
