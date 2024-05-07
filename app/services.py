from app import db
from app.models import User
from passlib.hash import pbkdf2_sha256
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

def register_user(username, password):
    hashed_password = pbkdf2_sha256.hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and pbkdf2_sha256.verify(password, user.password):
        return user