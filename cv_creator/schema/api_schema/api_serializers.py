from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, validator, root_validator, Extra


class SkillSchema(BaseModel):
    skill_name: str
    id: Optional[int] = None

    class Config:
        extra = Extra.forbid

    @validator('skill_name')
    def skill_name_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError('skill_name must be str')
        return v

    @validator('id')
    def skill_id_must_be_int(cls, v):
        if not isinstance(v, int):
            raise ValueError('id must be int')
        return v


class CompanySchema(BaseModel):
    company_name: str
    company_id: Optional[int] = None

    class Config:
        extra = Extra.forbid

    @validator('company_name')
    def company_name_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError('company_name must be str')
        return v

    @validator('company_id')
    def company_id_must_be_int(cls, v):
        if not isinstance(v, int):
            raise ValueError('company_id must be int')
        return v


class UserExperienceSchema(BaseModel):
    company: CompanySchema
    job_description: str
    start_date: datetime
    end_date: datetime

    class Config:
        extra = Extra.forbid

    @validator('company')
    def company_must_be_company_schema(cls, v):
        if not isinstance(v, CompanySchema):
            raise ValueError('company must be CompanySchema')
        return v

    @validator('job_description')
    def job_description_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError('job_description must be str')
        return v

    @validator('start_date')
    def start_date_must_be_datetime(cls, v):
        if not isinstance(v, datetime):
            raise ValueError('start_date must be datetime')
        return v

    @validator('end_date')
    def end_date_must_be_datetime(cls, v):
        if not isinstance(v, datetime):
            raise ValueError('end_date must be datetime')
        return v


class UserSkillsSchema(BaseModel):
    skill: SkillSchema
    skill_level: int

    class Config:
        extra = Extra.forbid

    @validator('skill_level')
    def skill_level_must_be_between_1_and_5(cls, v):
        if v < 1 or v > 5:
            raise ValueError('Skill level must be between 1 and 5')
        return v

    @validator('skill')
    def skill_must_be_skill_schema(cls, v):
        if not isinstance(v, SkillSchema):
            raise ValueError('skill must be SkillSchema')
        return v


class UserSchema(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    permission: str
    user_experience: List[UserExperienceSchema]
    user_skills: List[UserSkillsSchema]

    class Config:
        extra = Extra.forbid

    @validator('first_name')
    def first_name_must_be_string(cls, v):
        if not isinstance(v, str):
            raise ValueError('first_name must be a string')
        return v

    @validator('last_name')
    def last_name_must_be_string(cls, v):
        if not isinstance(v, str):
            raise ValueError('last_name must be a string')
        return v

    @validator('permission')
    def permission_must_be_string(cls, v):
        if not isinstance(v, str):
            raise ValueError('permission must be a string')
        return v

    @validator('user_experience')
    def user_experience_must_be_list(cls, v):
        if not isinstance(v, list):
            raise ValueError('user_experience must be a list')
        return v

    @validator('user_skills')
    def user_skills_must_be_list(cls, v):
        if not isinstance(v, list):
            raise ValueError('user_skills must be a list')
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
