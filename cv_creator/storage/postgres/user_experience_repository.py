from cv_creator.models.models import UserExperience
from cv_creator.storage.postgres.db_models import UserExperienceDb


class UserExperienceRepository:
    def __init__(self, db):
        self.db = db

    def get_user_experience_by_user_id(self, user_id: int) -> list[UserExperienceDb]:
        experiences = self.db.all(UserExperienceDb, user_id)
        return experiences

    def add_user_experience(
        self, user_id: int, user_experience: UserExperience
    ) -> UserExperienceDb:
        experience_dict = user_experience.to_dict()
        experience_dict["user_id"] = user_id
        experience_db: UserExperienceDb = UserExperienceDb(**experience_dict)
        self.db.add(experience_db)
        self.db.commit()
        return experience_db

    def delete_experience(self, user_experience_db: UserExperienceDb) -> None:
        self.db.delete(user_experience_db)
        self.db.commit()

    def get_user_experience_by_user_experience_id(self, user_experience_id):
        experience = self.db.get(UserExperienceDb, user_experience_id)
        return experience

    def update_user_experience(
        self, user_experience_id: int, user_experience: UserExperience
    ) -> UserExperienceDb:
        experience_dict = user_experience.to_dict()
        self.db.query(UserExperienceDb).filter(
            UserExperienceDb.id == user_experience_id
        ).update(experience_dict)
        self.db.commit()
        return self.get_user_experience_by_user_experience_id(
            user_experience_id=user_experience_id
        )
