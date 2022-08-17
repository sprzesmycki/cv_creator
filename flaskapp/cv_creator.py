from flask import json, request, make_response

from .database import app, db, User, UserSchema


@app.route('/user', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def user():
    user_schema = UserSchema()
    if request.method == 'GET':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'POST':
        data = json.loads(request.data)  # todo probably context-type validation required and handling missing fields
        user_details = User(first_name=data['first_name'], last_name=data['last_name'], permission=data['permission'])
        db.session.add(user_details)
        db.session.commit()
        return make_response(
            user_schema.dump(user_details),
            200
        )
    if request.method == 'PUT':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'PATCH':
        return make_response(
            "I will do that sometime later",
            418
        )
    if request.method == 'DELETE':
        return make_response(
            "I will do that sometime later",
            418
        )


@app.route('/cv', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def cv():
    return "I will do that sometime later"


@app.route('/stats', methods=["GET"])  # todo should I user methods=["GET"] even if its default one?
def get_stats():
    return "I will do that sometime later"


if __name__ == '__main__':
    app.run()
