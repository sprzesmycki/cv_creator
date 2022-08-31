from sqlalchemy import select, update

from cv_creator.database import SessionLocal
from cv_creator.models.db_models import User

db = SessionLocal()


def get_user_by_user_id(user_id) -> User:
    stmt = select(User).where(User.id == user_id)
    user = getattr(db.execute(stmt).one(), 'User')
    return user  # ugly but works


def add_user(user) -> User:
    db_user = User(first_name=user.first_name, last_name=user.last_name,
                   permission=user.permission)
    db.add(db_user)
    db.commit()
    return db_user


def update_user(user) -> User:
    current_user = get_user_by_user_id(user_id=user.id)
    current_user.update(user)  # todo something smart will be there
    stmt = update(User).where(User.id == user.id).values()  # todo values? cannot pass an object?
    db.execute(stmt)
    return get_user_by_user_id(user_id=user.id)
