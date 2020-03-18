from app.main import db
import datetime
from flask import jsonify
from app.main.models.user import User
import json
from sqlalchemy.exc import SQLAlchemyError


def save_new_user(data):
    try:
        user = User.query.filter_by(user_name=data['user_name']).first()
        if not user:
            new_user = User(
                user_name=data['user_name'],
                name=data['name'],
                last_name=data['last_name'],
                social_network_id=data['social_network_id'],
            )
            user = save_changes(new_user)
            return messsage(True, "created", user)
        
        else:
            if user != None:
                obtain_user = get_user(data['user_name'])
                return messsage(True, "exists", obtain_user.id)
            else:
                return messsage_error(False,'error')
    except SQLAlchemyError as e:
        return messsage_error('False', e)


def get_all_users():
    users = User.query.all()
    

def get_user(user_name):
    return User.query.filter_by(user_name=user_name).first()

def get_id(id):
    return User.query.get(int(id))

def messsage(status, accion, user):
    return {"status": status, "message": accion, "user_id": user}


def messsage_error(status, accion):
    return {"status": status, "message": accion}


def save_changes(data):
    db.session.add(data)
    db.session.commit()
    db.session.flush()
    data.id
    db.session.refresh(data)
    return data.id
