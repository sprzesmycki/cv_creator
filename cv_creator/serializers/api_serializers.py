from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from cv_creator.models.models import User, Skill, Company, UserExperience, UserSkills


class SkillSchema(BaseModel):
    skill_name: str
    skill_id: Optional[int] = None

    class Config:
        orm_mode = True

    @staticmethod
    def from_json(data):
        return SkillSchema(
            skill_name=data['skill_name'],
            skill_id=data['skill_id'],
        )

    @staticmethod
    def from_model(data):
        return SkillSchema(
            skill_name=data.skill_name,
            skill_id=data.skill_id,
        )

    @staticmethod
    def to_model(data):
        return Skill(
            skill_name=data.skill_name,
            skill_id=data.skill_id,
        )

    @staticmethod
    def to_json(data):
        return SkillSchema(
            skill_name=data.skill_name,
            skill_id=data.skill_id,
        )


class CompanySchema(BaseModel):
    company_name: str
    company_id: Optional[int] = None

    class Config:
        orm_mode = True

    @staticmethod
    def from_json(data):
        return CompanySchema(
            company_name=data['company_data'],
            company_id=data['company_id'],
        )

    @staticmethod
    def from_model(data):
        return CompanySchema(
            company_name=data.company_name,
            company_id=data.company_id,
        )

    @staticmethod
    def to_model(data):
        return Company(
            company_name=data.company_name,
            company_id=data.company_id,
        )

    @staticmethod
    def to_json(data):
        return CompanySchema(
            company_name=data.company_name,
            company_id=data.company_id,
        )


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

    @staticmethod
    def from_model(data):
        return UserExperienceSchema(
            company=CompanySchema.from_model(data.company),
            job_description=data.job_description,
            start_date=data.start_date,
            end_date=data.end_date,
        )

    @staticmethod
    def to_model(data):
        return UserExperience(
            company=CompanySchema.to_model(data.company),
            job_description=data.job_description,
            start_date=data.start_date,
            end_date=data.end_date,
        )

    @staticmethod
    def to_json(data):
        return UserExperienceSchema(
            company=CompanySchema.to_json(data.company),
            job_description=data.job_description,
            start_date=data.start_date,
            end_date=data.end_date,
        )


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

    @staticmethod
    def from_model(data):
        return UserSkillsSchema(
            skill=SkillSchema.from_model(data.skill),
            skill_level=data.skill_level,
        )

    @staticmethod
    def to_model(data):
        return UserSkills(
            skill=SkillSchema.to_model(data.skill),
            skill_level=data.skill_level,
        )

    @staticmethod
    def to_json(data):
        return UserSkillsSchema(
            skill=SkillSchema.to_json(data.skill),
            skill_level=data.skill_level,
        )


class UserSchema(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    phone_number: str
    user_experience: List[UserExperienceSchema]
    user_skills: List[UserSkillsSchema]

    class Config:
        orm_mode = True

    @staticmethod
    def from_json(data):
        return UserSchema(
            user_id=data['user_id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number'],
            user_experience=[UserExperienceSchema.from_json(x) for x in data['user_experience']],
            user_skills=[UserSkillsSchema.from_json(x) for x in data['user_skills']],
        )

    @staticmethod
    def from_model(data):
        return UserSchema(
            user_id=data.user_id,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            phone_number=data.phone_number,
            user_experience=[UserExperienceSchema.from_model(x) for x in data.user_experience],
            user_skills=[UserSkillsSchema.from_model(x) for x in data.user_skills],
        )

    @staticmethod
    def to_model(data):
        return User(
            user_id=data.user_id,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            phone_number=data.phone_number,
            user_experience=[UserExperienceSchema.to_model(x) for x in data.user_experience],
            user_skills=[UserSkillsSchema.to_model(x) for x in data.user_skills],
        )

    @staticmethod
    def to_json(data):
        return UserSchema(
            user_id=data.user_id,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            phone_number=data.phone_number,
            user_experience=[UserExperienceSchema.to_json(x) for x in data.user_experience],
            user_skills=[UserSkillsSchema.to_json(x) for x in data.user_skills],
        )
