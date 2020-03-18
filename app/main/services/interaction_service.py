from app.main import db
import datetime

from app.main.models.interaction import Interaction
from sqlalchemy.exc import SQLAlchemyError

def save_new_interaction(data):
    interaction = Interaction.query.filter_by(user_id=data['user_id']).first()

    try:
        if not interaction:
            new_Interaction = Interaction(
                user_id=data['user_id'],
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
    except Exception as e:
        print(e)
        return messsage_error('False', e)

def get_all_interactions():
    return Interaction.query.all()


def messsage_error(status, accion):
    return {"status": status, "message": accion}

def messsage(status, accion, user):
    return {"status": status, "message": accion, "user_id": user}

def save_changes(data):
    db.session.add(data)
    db.session.commit()