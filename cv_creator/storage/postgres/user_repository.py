from cv_creator.models.models import User, UpdateUser
from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.db_models import UserDb


class UserRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_user_by_user_id(self, user_id: int) -> UserDb:
        user = self.db.get(UserDb, user_id)
        return user

    def add_user(self, user: User) -> UserDb:
        user_dict = user.to_dict()
        user_db: UserDb = UserDb(**user_dict)
        self.db.add(user_db)
        self.db.commit()
        return user_db

    def delete_user(self, user: UserDb) -> None:
        self.db.delete(user)
        self.db.commit()

    def update_user(self, user_id: int, user: UpdateUser) -> UserDb:
        user_dict = user.to_dict()
        self.db.query(UserDb).filter(UserDb.id == user_id).update(user_dict)
        self.db.commit()
        return self.get_user_by_user_id(user_id=user_id)
