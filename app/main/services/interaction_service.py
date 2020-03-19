from app.main import db
import datetime

from app.main.models.interaction import Interaction
from sqlalchemy.exc import SQLAlchemyError
from app.main.util.utils import messsage_error, messsage

def save_new_interaction(data):
    # print(data)
    try:
        new_interaction = Interaction(
            user_id=data['user_id'],
            input_db=data['input_db'],
            output_db=data['output_db'],
            registered_on=datetime.datetime.utcnow()
        )
        interaction = save_changes(new_interaction)
        return {"status":True}
    except SQLAlchemyError as e:
        return messsage_error('False', e)


def get_all_interactions():
    data = Interaction.query.all()
    return data



def save_changes(data):
    db.session.add(data)
    db.session.commit()
    db.session.flush()
    data.id
    db.session.refresh(data)
    return data.id
