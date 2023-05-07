from werkzeug.security import generate_password_hash

from blog.app import create_app, db

# from blog.models import *

app = create_app()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User

    db.session.add(
        User(email='name@email.com', password=generate_password_hash('test123'))
    )
    db.session.commit()
