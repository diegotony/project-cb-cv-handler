from .. import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255))
    name = db.Column(db.String(255))
    last_name= db.Column(db.String(255))
    social_network_id=db.Column(db.String(255))
    

"""
{'user': {'user_name': 'astandre', 'name': 'André', 'last_name': 'Herrera', 'social_network_id': 614535395}, 'comando': '/PrevencionTransporte'}
"""

