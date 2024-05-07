from app import app, db
from app.models import User
from app.services import register_user, authenticate
from flask import request, jsonify
from datetime import datetime, timedelta
from app import generate_jwt_token
import jwt

def authenticate_user(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user_id = payload['sub']
        user = User.query.get(user_id)
        return user
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Endpoint para registro
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    register_user(username, password)
    return jsonify({'message': 'User created successfully'})

# Endpoint para login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = authenticate(username, password)
    if user:
        token = generate_jwt_token(user.id)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

# Endpoint protegido teste
@app.route('/teste', methods=['GET'])
def teste():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401

    user = authenticate_user(token)
    if not user:
        return jsonify({'message': 'Invalid token'}), 401

    # Se o usuário estiver autenticado, continue com a lógica da rota
    return jsonify({'message': 'This is a protected route'})
