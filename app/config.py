import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY",
                                    "your-jwt-secret-key")
    JWT_HEADER_TYPE = os.getenv('JWT_HEADER_TYPE', '')
