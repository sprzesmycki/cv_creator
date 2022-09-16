from cv_creator.database import SessionLocal
from cv_creator.models.db_models import UserDb
from cv_creator.serializers.api_serializers import UserSchema
from cv_creator.serializers.db_serializers import PostUserSchema

db = SessionLocal()


def get_user_by_user_id(user_id) -> UserDb:
    return db.query(UserDb).filter(UserDb.id == user_id).first()


def add_user(post_user) -> UserDb:
    user_api = UserSchema().dump(post_user)
    user_db = PostUserSchema().load(user_api, session=db)
    db.add(user_db)
    db.commit()
    return user_db


def update_user(user_id, patch_user) -> UserDb:
    user = get_user_by_user_id(user_id)
    if user is not None:
        db.query(UserDb).filter(UserDb.id == user_id).update(patch_user)
        db.commit()
        return get_user_by_user_id(user_id=user.id)


def delete_user(user_id):
    user = db.get(UserDb, user_id)
    if user is not None:
        db.delete(user)
        db.commit()
