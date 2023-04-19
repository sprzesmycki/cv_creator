from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from cv_creator.storage.postgres.database import Base


class UserDb(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    permission = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"


class SkillDb(Base):
    __tablename__ = "skill"
    id = Column(Integer, primary_key=True)
    skill_name = Column(String, nullable=False, unique=True)

    # add relation many to many with user
    def __repr__(self) -> str:
        return f"Skills(id={self.id!r}, skill_name={self.skill_name!r}"


class UserSkillsDb(Base):
    __tablename__ = "user_skills"
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, primary_key=True)
    skill_id = Column(Integer, ForeignKey("skill.id"), nullable=False, primary_key=True)
    skill_level = Column(Integer, nullable=False)

    user = relationship("UserDb", backref="user_skills")
    skill = relationship("SkillDb", backref="user_skills")

    def __repr__(self) -> str:
        return (
            f"UserSkills(id={self.id!r}, user_id={self.user_id!r}, "
            f"skill_id={self.skill_id!r}, skill_level={self.skill_level!r}) "
        )


class CompanyDb(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Company(id={self.id!r}, company_name={self.user_id!r}"


class UserExperienceDb(Base):
    __tablename__ = "user_experience"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    job_description = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    user = relationship("UserDb", backref="user_experience")
    company = relationship("CompanyDb", backref="user_experience")

    def __repr__(self) -> str:
        return (
            f"UserExperience(id={self.id!r}, user_id={self.user_id!r}, "
            f"company_name={self.company_name!r}, job_description={self.job_description!r}), "
            f"start_date={self.start_date!r}, end_date={self.end_date!r}) "
        )
