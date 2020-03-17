from app.main import db
import datetime
from flask import jsonify
from app.main.models.user import User
import json

def save_new_user(data):
    try:
        if User.query.filter_by(user_name=data['user_name']) != None:
            user = User.query.filter_by(user_name=data['user_name']).one()
            return messsage(True,"exists",user.id)
        else:
            new_user = User(
                user_name=data['user_name'],
                name=data['name'],
                last_name=data['last_name'],
                social_network_id=data['social_network_id'],
                )
            save_changes(new_user)
            user = get_user(data['user_name'])
            return messsage(True,"created",user.id)
        
    except Exception as e:
        return messsage_error('False',"error")

def get_all_users():
    return User.query.all()

def get_user(user_name):
    return User.query.filter_by(user_name=user_name).first()


def messsage(status,accion,user):
    return {"status":status,"message":accion,"user_id":user}

def messsage_error(status,accion):
    return {"status":status,"message":accion}



def save_changes(data):
    db.session.add(data)
    db.session.commit()
