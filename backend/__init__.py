from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from backend.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    from backend.routes import second

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(second)

    return app
