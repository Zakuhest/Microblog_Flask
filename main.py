from app import create_app
from app.db import db
from app.login import Login

app = create_app()

Login.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()