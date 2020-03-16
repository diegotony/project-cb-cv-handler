from .. import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    last_name= db.Column(db.String(255))
    username =db.Column(db.String(255))


