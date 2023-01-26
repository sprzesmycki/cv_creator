from cv_creator.models.models import User
from cv_creator.serializers.db_serializers import user_schema_without_id
from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.storage.postgres.db_models import UserDb

db = SessionLocal()


def get_user_by_user_id(user_id: int) -> UserDb:
    user = db.get(UserDb, user_id)
    return user


def add_user(user: User) -> UserDb:
    user_db = user_schema_without_id.load(user, session=db)
    db.add(user_db)
    db.commit()
    return user_db


def delete_user(user: UserDb) -> None:
    db.delete(user)
    db.commit()


def update_user(user: User) -> UserDb:
    user_db = user_schema_without_id.load(user, session=db)
    db.query(UserDb).filter(UserDb.id == user.id).update(user_db)
    db.commit()
    return get_user_by_user_id(user_id=user.id)
