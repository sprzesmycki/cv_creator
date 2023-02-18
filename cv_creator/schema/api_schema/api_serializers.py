from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, validator, root_validator


class SkillSchema(BaseModel):
    skill_name: str
    skill_id: Optional[int] = None

    class Config:
        orm_mode = True

    @staticmethod
    def from_json(data):
        return SkillSchema(
            skill_name=data['skill_name'],
            skill_id=data['id'],
        )

    @validator('skill_name')
    def skill_name_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError('skill_name must be str')
        return v

    @validator('skill_id')
    def skill_id_must_be_int(cls, v):
        if not isinstance(v, int):
            raise ValueError('skill_id must be int')
        return v


class CompanySchema(BaseModel):
    company_name: str
    company_id: Optional[int] = None

    class Config:
        orm_mode = True

    @staticmethod
    def from_json(data):
        return CompanySchema(
            company_name=data['company_data'],
            company_id=data['id'],
        )

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
        orm_mode = True

    @staticmethod
    def from_json(data):
        return UserExperienceSchema(
            company=CompanySchema.from_json(data['company']),
            job_description=data['job_description'],
            start_date=data['start_date'],
            end_date=data['end_date'],
        )

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
        orm_mode = True

    @staticmethod
    def from_json(data):
        return UserSkillsSchema(
            skill=SkillSchema.from_json(data['skill']),
            skill_level=data['skill_level'],
        )

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
        orm_mode = True

    @staticmethod
    def from_json(data):
        return UserSchema(
            id=data.get('id'),
            first_name=data['first_name'],
            last_name=data['last_name'],
            permission=data['permission'],
            user_experience=[UserExperienceSchema.from_json(x) for x in data['user_experience']],
            user_skills=[UserSkillsSchema.from_json(x) for x in data['user_skills']],
        )

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

    # it checks after from_json method - so its worthless
    @root_validator
    def check_extra_fields(cls, values):
        unexpected_fields = set(values.keys()) - set(cls.__fields__.keys())
        if unexpected_fields:
            raise ValueError(f"Unexpected field(s): {', '.join(unexpected_fields)}")
        return values
