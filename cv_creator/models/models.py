from dataclasses import field, dataclass, asdict
from datetime import datetime
from typing import List, Optional, Any, Dict


@dataclass
class Skill:
    skill_name: str
    skill_id: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v}


@dataclass
class Company:
    company_name: str
    company_id: Optional[int] = None


@dataclass
class UserExperience:
    company: Company
    job_description: str
    start_date: datetime
    end_date: datetime
    id: Optional[int] = field(default=None, repr=False)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v}


@dataclass
class UpdateUserExperience:
    company: Company
    job_description: str
    start_date: datetime
    end_date: datetime
    id: Optional[int] = field(default=None, repr=False)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v}


@dataclass
class UserSkills:
    skill: Skill
    skill_level: int


@dataclass
class User:
    first_name: str
    last_name: str
    permission: str
    id: Optional[int] = field(default=None, repr=False)
    user_skills: List[UserSkills] = field(default_factory=list)
    user_experience: List[UserExperience] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v}


@dataclass
class UpdateUser:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    permission: Optional[str] = None
    id: Optional[int] = field(default=None, repr=False)
    user_skills: List[UserSkills] = field(default_factory=list)
    user_experience: List[UserExperience] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v}
