from app import db
from app.models import User, Role, UserRole
import hashlib
import binascii

# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

def register_user(username, password):
    # hashed_password = pbkdf2_sha256.hash(password)
    # new_user = User(username=username, password=hashed_password)
    # db.session.add(new_user)
    # db.session.commit()
    pass

def verify_password(password, hash):
    parts = hash.split('$')
    if len(parts) == 3:
        algorithm, salt, stored_hash = parts
        iterations = 260000
    elif len(parts) == 4:
        algorithm, iterations, salt, stored_hash = parts
        iterations = int(iterations)
    else:
        raise ValueError("Formato de hash inválido")
    
    new_hash = hashlib.pbkdf2_hmac(algorithm.split(':')[1], password.encode('utf-8'), salt.encode('utf-8'), iterations)

    return new_hash == binascii.unhexlify(stored_hash)

def authenticate(username, inputPassword):
    results = db.session.query(User.id, User.username, User.password, Role.name)\
        .join(UserRole, User.id == UserRole.user_id)\
        .join(Role, UserRole.role_id == Role.id)\
        .filter(User.username == username)\
        .all()

    authenticated_user = None

    for id, username, password, role_name in results:
        if not authenticated_user:
            authenticated_user = {"id": id, "username": username, "password": password, "roles": []}
        authenticated_user["roles"].append(role_name)

    if authenticated_user:
        if verify_password(inputPassword, authenticated_user['password']):
            return authenticated_user

    return None