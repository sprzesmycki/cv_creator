from typing import Optional

from cv_creator.models.models import Skill
from cv_creator.schema.db_schema.db_serializers import skill_db_schema
from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.db_models import SkillDb
from cv_creator.storage.postgres.skill_repository import SkillRepository


def get_skill_by_skill_id(skill_id: int) -> Optional[Skill]:
    db = SessionLocal()
    skill_db: SkillDb = SkillRepository(db).get_skill_by_skill_id(skill_id)
    if skill_db is not None:
        skill_dict: dict = skill_db_schema.dump(skill_db)
        skill: Skill = Skill(**skill_dict)
        return skill
    else:
        return None


def add_skill(post_skill: Skill) -> Skill:
    db = SessionLocal()
    skill_db: SkillDb = SkillRepository(db).add_skill(post_skill)
    skill_dict: dict = skill_db_schema.dump(skill_db)
    skill: Skill = Skill(**skill_dict)
    return skill


def delete_skill(skill_id: int) -> None:
    db = SessionLocal()
    skill_db: SkillDb = SkillRepository(db).get_skill_by_skill_id(skill_id)
    if skill_db is not None:
        SkillRepository(db).delete_skill(skill_db)
    else:
        raise ValueError("Skill does not exist")
