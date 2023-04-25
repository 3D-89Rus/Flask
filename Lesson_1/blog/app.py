from flask import Flask
from Lesson_1.blog.views.users import users_app
from Lesson_1.blog.views.articles import articles_app


def register_blueprints(app: Flask):
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(users_app, url_prefix="/users")


app = Flask(__name__)
