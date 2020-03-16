from .. import db

class Interaction(db.Model):
    __tablename__ = "interaction"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    input_db = db.Column(db.String(255))
    output_db = db.Column(db.String(255))
    registered_on = db.Column(db.DateTime, nullable=False)
   

