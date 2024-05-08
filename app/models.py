from app import db

class User(db.Model):
    __tablename__ = 'ab_user'

    id = db.Column(db.Integer, primary_key=True)
    changed_by_fk = db.Column(db.Integer)
    fail_login_count = db.Column(db.Integer)
    created_on = db.Column(db.DateTime)
    changed_on = db.Column(db.DateTime)
    created_by_fk = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    last_login = db.Column(db.DateTime)
    login_count = db.Column(db.Integer)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))

class Role(db.Model):
    __tablename__ = 'ab_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class UserRole(db.Model):
    __tablename__ = 'ab_user_role'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)