from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_moment import Moment
from app.routes.auth import auth_router
from app.routes.index import index_router
from app.routes.users import users_router
from app.routes.posts import posts_router


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_router)
    app.register_blueprint(index_router)
    app.register_blueprint(users_router)
    app.register_blueprint(posts_router)

    login = LoginManager(app)
    db = SQLAlchemy(app)
    Moment(app)
    Migrate(app,db)

    return app