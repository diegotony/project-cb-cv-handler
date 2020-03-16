from app.main import db
import datetime

from app.main.models.user import User


def save_new_user(data):
    user = User.query.filter_by(user_name=data['user_name']).first()
    if not user:
        new_user = User(
            user_name=data['user_name'],
            name=data['name'],
            last_name=data['last_name'],
            social_network_id=data['social_network_id'],
        )
        save_changes(new_user)
        # response_object = {
        #     'status': 'success',
        #     'message': 'Successfully registered.'
        # }
        # return response_object, 201
        return 0
    else:
        # response_object = {
        #     'status': 'fail',
        #     'message': 'user already exists. Please Log in.',
        # }
        # return response_object, 409
        return 1


# def get_all_users():
#     return user.query.all()


# def get_a_user(public_id):
#     return user.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
