from app import app
from db import db


db.innit_app(app)


@app.before_first_request
def create_tables():
    db.create_all()