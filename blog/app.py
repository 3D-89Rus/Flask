from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
db = SQLAlchemy()
__all__ = [
    "db",
]


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'k*ulna*oz1^#^a_+k3e=7hr+ecenfl_tco#49-a38s64@=+o(7'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.auth.views import auth
    from blog.report.views import report
    from blog.user.views import user

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(auth)
