from cv_creator.models.models import Skill
from cv_creator.storage.postgres.db_models import UserSkillsDb, SkillDb


class SkillRepository:
    def __init__(self, db):
        self.db = db

    def get_users_count_with_skill(self, skill_id, skill_level):
        return (
            self.db.query(UserSkillsDb)
            .filter(
                UserSkillsDb.skill_id == skill_id,
                UserSkillsDb.skill_level == skill_level,
            )
            .count()
        )

    def get_skill_by_skill_id(self, skill_id: int) -> SkillDb:
        skill = self.db.get(SkillDb, skill_id)
        return skill

    def add_skill(self, skill: Skill) -> SkillDb:
        skill_dict = skill.to_dict()
        skill_db: SkillDb = SkillDb(**skill_dict)
        self.db.add(skill_db)
        self.db.commit()
        return skill_db

    def delete_skill(self, skill_db: SkillDb) -> None:
        self.db.delete(skill_db)
        self.db.commit()
