from cv_creator.storage.postgres.db_models import UserSkillsDb


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
