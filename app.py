from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://@107.216.161.65/student_project"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello_world():
    for user in Users.query.all():
        print(user)
    return ""

if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
