from flask import Flask
from sqlalchemy import Table, create_engine, MetaData
from sqlalchemy.future import engine
from sqlalchemy.orm import mapper

app = Flask(__name__)


class User(object):

    def __init__(self, id=None, firstName=None, lastName=None, bday=None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.bday = bday

    def __repr__(self):
        return f'<User {self.firstName}:{self.lastName}>'


metadata = MetaData(bind=engine)
users = Table('users', metadata, autoload=True)
mapper(User, users)


@app.route('/')
def hello_world():
    engine = create_engine(
        "mysql+pymysql://:@107.216.161.65/student_project"
    )
    conn = engine.connect()
    results = conn.execute(User, "select * from student_project.users")
    print(results)
    for u in results:
        print(u)
    return "Hello world"


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
