from flask import json, request

from .database import app, db, User


@app.route('/add_user', methods=["POST"])
def add_user():
    data = json.loads(request.data)  # todo probably context-type validation required and handling missing fields
    user = User(first_name=data['first_name'], last_name=data['last_name'], permission=data['permission'])
    db.session.add(user)
    db.session.commit()
    return repr(user)


if __name__ == '__main__':
    app.run()
