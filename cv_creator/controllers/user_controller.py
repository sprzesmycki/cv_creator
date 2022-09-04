from cv_creator.database import SessionLocal
from cv_creator.models.db_models import User
from cv_creator.serializers.db_serializers import CompleteUserSchema

db = SessionLocal()


def get_user_by_user_id(user_id) -> User:
    return db.query(User).filter(User.id == user_id).first()


def add_user(request) -> User:
    schema = CompleteUserSchema()
    user = schema.load(request.json, session=db)
    db.add(user)
    db.commit()
    return user


def update_user(request) -> User:
    schema = CompleteUserSchema()
    user_id = request.json.get('id')
    user = db.query(User).get(user_id)
    schema.load(request.json, instance=user, partial=True, session=db)
    return get_user_by_user_id(user_id=user.id)


def delete_user(user_id):
    user = db.get(User, user_id)
    if user is not None:
        db.delete(user)
        db.commit()
