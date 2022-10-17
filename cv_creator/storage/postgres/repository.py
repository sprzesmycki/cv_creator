from cv_creator.storage.postgres.database import SessionLocal
from cv_creator.serializers.api_serializers import UserSchema
from cv_creator.serializers.db_serializers import PostUserSchema
from cv_creator.storage.postgres.db_models import UserDb

db = SessionLocal()


def get_user_by_user_id(user_id) -> UserDb:
    user = db.get(UserDb, user_id)
    return user


def add_user(post_user):
    user_api = UserSchema().dump(post_user)
    user_db = PostUserSchema().load(user_api, session=db)
    db.add(user_db)
    db.commit()
    return user_db


def update_user(patch_user, user, user_id):
    db.query(UserDb).filter(UserDb.id == user_id).update(patch_user)
    db.commit()
    return get_user_by_user_id(user_id=user.id)


def delete_user(user: UserDb):
    db.delete(user)
    db.commit()
