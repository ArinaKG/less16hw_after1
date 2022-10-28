import json
from less16hw_after1 import models
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def load_data(filename):
    json_data = []
    with open(filename) as file:
        json_data = json.load(file)

    return json_data


def load_users(filename):
    users = load_data(filename)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)

    db.session.commit()