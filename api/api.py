import time
from flask import Flask, g
from flask import request
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth
from vm import start_vm, stop_vm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    access = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.username

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


# db.create_all()


@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    access = request.json.get('access')
    print(access, flush=True)
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)  # existing user
    user = User(username=username, access=access)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return {'username': user.username}, 201


# @auth.verify_password
# def verify_password(username, password):
#     username = request.json.get('username')
#     password = request.json.get('password')
#     user = User.query.filter_by(username=username).first()
#     if not user or not user.verify_password(password):
#         print('HOHOHO', flush=True)
#         print(username, flush=True)
#         print(password, flush=True)
#         print(user, flush=True)
#         return False
#     g.user = user
#     print(g.user, flush=True)
#     return True


# @auth.error_handler
# def unauthorized():
#     return {'error': 'error'}, 401


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
    return {'response': 'true', 'username': user.username, 'access': user.access}


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/vm/start/<vm_number>')
def play(vm_number):
    response = start_vm(int(vm_number))
    return {'response': '{}'.format(response)}


@app.route('/api/vm/stop/<vm_number>')
def stop(vm_number):
    response = stop_vm(int(vm_number))
    return {'response': '{}'.format(not response)}
