from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, validator, Extra


class SkillSchema(BaseModel):
    skill_name: str
    id: Optional[int] = None

    class Config:
        extra = Extra.forbid

    @validator("skill_name")
    def skill_name_must_be_shorter_than_20_chars(cls, v):
        if len(v) > 20:
            raise ValueError("skill_name must be shorter than 20 chars")
        return v


class CompanySchema(BaseModel):
    company_name: str
    company_id: Optional[int] = None

    class Config:
        extra = Extra.forbid


class UserExperienceSchema(BaseModel):
    user_experience_id: Optional[int] = None
    company: CompanySchema
    job_description: str
    start_date: datetime
    end_date: datetime

    class Config:
        extra = Extra.forbid


class UpdateUserExperienceSchema(BaseModel):
    user_experience_id: int
    company: Optional[CompanySchema] = None
    job_description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        extra = Extra.forbid


class UserSkillsSchema(BaseModel):
    skill: SkillSchema
    skill_level: int

    class Config:
        extra = Extra.forbid

    @validator("skill_level")
    def skill_level_must_be_between_1_and_5(cls, v):
        if v < 1 or v > 5:
            raise ValueError("Skill level must be between 1 and 5")
        return v


class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    permission: str

    class Config:
        extra = Extra.forbid

    @validator("permission")
    def permission_must_be_admin_or_user(cls, v):
        if v != "admin" and v != "user":  # problably should use some kind of enum
            raise ValueError("Permission must be admin or user")
        return v


class UpdateUserSchema(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    permission: Optional[str] = None
    user_experience: Optional[List[UserExperienceSchema]] = None
    user_skills: Optional[List[UserSkillsSchema]] = None

    class Config:
        extra = Extra.forbid

    @validator("permission")
    def permission_must_be_admin_or_user(cls, v):
        if v != "admin" and v != "user":  # probably should use some kind of enum
            raise ValueError("Permission must be admin or user")
        return v


class UserArgsSchema(BaseModel):
    user_id: int

    class Config:
        extra = Extra.forbid


class SkillArgsSchema(BaseModel):
    skill_id: int

    class Config:
        extra = Extra.forbid


class StatsArgsSchema(BaseModel):
    skill_id: int
    skill_level: int

    class Config:
        extra = Extra.forbid
