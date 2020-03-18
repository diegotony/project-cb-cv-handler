from flask_restplus import Namespace, fields


class InteractionDto:
    api = Namespace(
        'interaction', description='interaction related operations')
    interaction = api.model('interaction', {
        'user_id': fields.Integer(required=True, description='user id'),
        'input_db': fields.String(required=True, description='input'),
        'output_db': fields.String(required=True, description='output'),
    })


class CommandDto:
    api = Namespace('command', description='commands')
    command = api.model('command', {
        'user_name': fields.String(required=False, description='user name'),
        'name': fields.String(required=False, description='name'),
        'last_name': fields.String(required=False, description='last name'),
        'social_network_id': fields.String(required=False, description='last name'),
        'command': fields.String(required=True, description='last name'),
    })

