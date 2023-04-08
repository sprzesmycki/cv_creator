from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.stats_repository import SkillRepository


def get_users_count_with_skill(skill_id, skill_level):
    db = SessionLocal()
    users_count = SkillRepository(db).get_users_count_with_skill(skill_id, skill_level)
    return users_count
