import time
from flask import Flask, g
from flask.helpers import url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)  # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return {'username': user.username}, 201


@auth.verify_password
def verify_password(username, password):
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        print('HOHOHO', flush=True)
        print(username, flush=True)
        print(password, flush=True)
        print(user, flush=True)
        return False
    g.user = user
    print(g.user, flush=True)
    return True


@auth.error_handler
def unauthorized():
    return {'error': 'error'}, 401


@app.route('/api/resource', methods=['POST'])
def verify_password():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        print('HOHOHO', flush=True)
        print(username, flush=True)
        print(password, flush=True)
        print(user, flush=True)
        return {'response': 'false'}
    g.user = user
    print(g.user, flush=True)
    return {'response': 'true'}


@app.route('/time')
def get_current_time():
    return {'time': time.time()}
