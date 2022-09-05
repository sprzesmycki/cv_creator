from cv_creator.database import SessionLocal
from cv_creator.models.db_models import User

db = SessionLocal()


def get_user_by_user_id(user_id) -> User:
    return db.query(User).filter(User.id == user_id).first()


def add_user(post_user) -> User:
    db.add(post_user)
    db.commit()
    return post_user


def update_user(user_id, patch_user) -> User:
    user = get_user_by_user_id(user_id)
    if user is not None:
        db.query(User).filter(User.id == user_id).update(patch_user)
        db.commit()
        return get_user_by_user_id(user_id=user.id)


def delete_user(user_id):
    user = db.get(User, user_id)
    if user is not None:
        db.delete(user)
        db.commit()
