from cv_creator.models.models import User, UpdateUser
from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.db_models import UserDb

db = SessionLocal()


def get_user_by_user_id(user_id: int) -> UserDb:
    user = db.get(UserDb, user_id)
    return user


def add_user(user: User) -> UserDb:
    user_dict = user.to_dict()
    user_db: UserDb = UserDb(**user_dict)
    db.add(user_db)
    db.commit()
    return user_db


def delete_user(user: UserDb) -> None:
    db.delete(user)
    db.commit()


def update_user(user_id: int, user: UpdateUser) -> UserDb:
    user_dict = user.to_dict()
    db.query(UserDb).filter(UserDb.id == user_id).update(user_dict)
    db.commit()
    return get_user_by_user_id(user_id=user_id)
