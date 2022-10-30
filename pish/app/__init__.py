
# ▄▀█ █▀█ █▀█
# █▀█ █▀▀ █▀▀

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Makes mysql work
import pymysql
pymysql.install_as_MySQLdb()


db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()


def create_app(config):
    app = Flask(__name__)
    app.config.from_mapping(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import models
    from app.views import views

    app.register_blueprint(models)
    app.register_blueprint(views)

    return app
