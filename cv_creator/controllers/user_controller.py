from flask import json
from sqlalchemy import select

from cv_creator import models
from cv_creator.database import SessionLocal

db = SessionLocal()


def get_user(user_id):
    stmt = select(models.User).where(models.User.id == user_id)
    return getattr(db.execute(stmt).one(), 'User')  # ugly but works


def add_user(request) -> models.User:
    data = json.loads(request.data)
    user_details = models.User(first_name=data['first_name'], last_name=data['last_name'],
                               permission=data['permission'])
    db.add(user_details)
    db.commit()
    return user_details
