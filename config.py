import os
from dotenv import load_dotenv
from pathlib import Path

# .env.prod = .env de prodição
# .env.dev = .env de desenvolvimento
dotenv_path = Path('.env.dev')
load_dotenv(dotenv_path=dotenv_path)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
