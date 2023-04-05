from datetime import datetime

from cv_creator.models.models import User, UserSkills, Skill, UserExperience, Company


def test_to_dict_for_user_model(client):
    time_now = str(datetime.now().date())
    user = User(
        first_name='John',
        last_name='Doe',
        permission='admin',
        id=1,
        user_skills=[UserSkills(skill=Skill(skill_name='Python'), skill_level=5)],
        user_experience=[
            UserExperience(
                company=Company(company_name='Google'),
                job_description='Software Engineer',
                start_date=time_now,
                end_date=time_now
            )
        ]
    )
    assert user.to_dict() == {'first_name': 'John', 'last_name': 'Doe', 'permission': 'admin', 'id': 1,
                              'user_skills': [{'skill': {'skill_name': 'Python', 'skill_id': None}, 'skill_level': 5}],
                              'user_experience': [{'company': {'company_name': 'Google', 'company_id': None},
                                                   'job_description': 'Software Engineer',
                                                   'start_date': time_now,
                                                   'end_date': time_now}]}
