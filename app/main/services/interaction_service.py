from app.main import db
import datetime

from app.main.models.interaction import Interaction

def save_new_interaction(data):
    interaction = Interaction.query.filter_by(user=data['user']).first()
    if not interaction:
        new_Interaction = Interaction(
            user=data['user'],
            input_db=data['input_db'],
            output_db=data['output_db'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_Interaction)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Interaction already exists. Please Log in.',
        }
        return response_object, 409


def get_all_interactions():
    return Interaction.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()