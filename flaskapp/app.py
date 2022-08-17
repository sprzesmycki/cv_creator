from flask import Flask
from sqlalchemy.orm import Session

from . import db

app = Flask(__name__)


@app.route('/add')
def add():
    with Session(db.engine) as session:
        test_user = db.Users(
            first_name='Seb',
            last_name='Prz',
            permission='admin'
        )

        session.add(test_user)
        session.commit()
        return repr(test_user)


if __name__ == '__main__':
    app.run()
