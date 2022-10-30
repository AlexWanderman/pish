from os import environ
from app import create_app

app = create_app({
    'DEBUG': False,
    'SECRET_KEY': environ.get('SECRET_KEY'),
    'SQLALCHEMY_DATABASE_URI': environ.get('SQLALCHEMY_DATABASE_URI')
})
