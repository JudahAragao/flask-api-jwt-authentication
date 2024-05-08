from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime, timedelta, timezone
import jwt

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Função para gerar token JWT
def generate_jwt_token(user_id, roles):
    payload = {
        'sub': user_id,
        'roles': roles,
        'exp': datetime.now(timezone.utc) + timedelta(days=1)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

from app import models, controllers

with app.app_context():
    db.create_all()
