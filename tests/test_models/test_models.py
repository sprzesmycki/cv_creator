from datetime import datetime

from cv_creator.models.models import (
    User,
    UserSkills,
    Skill,
    UserExperience,
    Company,
    UpdateUser,
    UpdateUserExperience,
)


def test_to_dict_for_user_model(client):
    time_now = datetime.now().date()
    user = User(
        first_name="John",
        last_name="Doe",
        permission="admin",
        id=1,
        user_skills=[UserSkills(skill=Skill(skill_name="Python"), skill_level=5)],
        user_experience=[
            UserExperience(
                company=Company(company_name="Google"),
                job_description="Software Engineer",
                start_date=time_now,
                end_date=time_now,
            )
        ],
    )
    assert user.to_dict() == {
        "first_name": "John",
        "last_name": "Doe",
        "permission": "admin",
        "id": 1,
        "user_skills": [
            {"skill": {"skill_name": "Python", "id": None}, "skill_level": 5}
        ],
        "user_experience": [
            {
                "company": {"company_name": "Google", "id": None},
                "job_description": "Software Engineer",
                "id": None,
                "start_date": time_now,
                "end_date": time_now,
            }
        ],
    }


def test_to_dict_for_update_user_model(client):
    time_now = datetime.now().date()
    user = UpdateUser(
        first_name="John",
        last_name="Doe",
        permission="admin",
        id=1,
        user_skills=[UserSkills(skill=Skill(skill_name="Python"), skill_level=5)],
        user_experience=[
            UserExperience(
                company=Company(company_name="Google"),
                job_description="Software Engineer",
                start_date=time_now,
                end_date=time_now,
            )
        ],
    )
    assert user.to_dict() == {
        "first_name": "John",
        "last_name": "Doe",
        "permission": "admin",
        "id": 1,
        "user_skills": [
            {"skill": {"skill_name": "Python", "id": None}, "skill_level": 5}
        ],
        "user_experience": [
            {
                "company": {"company_name": "Google", "id": None},
                "job_description": "Software Engineer",
                "id": None,
                "start_date": time_now,
                "end_date": time_now,
            }
        ],
    }


def test_to_dict_for_skill_model(client):
    skill = Skill(skill_name="Python", id=5)
    assert skill.to_dict() == {"skill_name": "Python", "id": 5}


def test_to_dict_for_company_model(client):
    company = Company(company_name="Google", id=5)
    assert company.to_dict() == {"company_name": "Google", "id": 5}


def test_to_dict_for_user_experience_model(client):
    time_now = datetime.now().date()
    user_experience = UserExperience(
        id=1,
        company=Company(company_name="Google"),
        job_description="Software Engineer",
        start_date=time_now,
        end_date=time_now,
    )
    assert user_experience.to_dict() == {
        "company": {"company_name": "Google", "id": None},
        "job_description": "Software Engineer",
        "id": 1,
        "start_date": time_now,
        "end_date": time_now,
    }


def test_to_dict_for_user_skills_model(client):
    user_skill = UserSkills(skill=Skill(skill_name="Python", id=5), skill_level=5)
    assert user_skill.to_dict() == {
        "skill": {"skill_name": "Python", "id": 5},
        "skill_level": 5,
    }


def test_to_dict_update_user_experience_model(client):
    time_now = datetime.now().date()
    user_experience = UpdateUserExperience(
        id=1,
        company=Company(company_name="Google"),
        job_description="Software Engineer",
        start_date=time_now,
        end_date=time_now,
    )
    assert user_experience.to_dict() == {
        "company": {"company_name": "Google", "id": None},
        "job_description": "Software Engineer",
        "id": 1,
        "start_date": time_now,
        "end_date": time_now,
    }
