from flask_restplus import Namespace, fields


class InteractionDto:
    api = Namespace('interaction', description='interaction related operations')
    interaction = api.model('interaction', {
        'user': fields.String(required=True, description='user email address'),
        'input_db': fields.String(required=True, description='user username'),
        'output_db': fields.String(required=True, description='user password'),
    })