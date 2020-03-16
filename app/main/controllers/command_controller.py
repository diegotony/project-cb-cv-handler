from flask import request
from flask_restplus import Resource

from ..util.dto import CommandDto
from ..util.commands import get_all_commands
from ..services.user_service import *

api = CommandDto.api
_command = CommandDto.command


@api.route('/')
class CommandList(Resource):
    @api.doc('list_of_registered_commands')
    # @api.marshal_list_with(_command, envelope='data')
    def get(self):
        """List all registered commands"""
        return get_all_commands()

    @api.response(201, 'Interaction successfully created.')
    @api.doc('create interaction with command')
    @api.expect(_command, validate=True)
    def post(self):
        """Creates a new Interaction """
        data = request.json
        user = {"user_name": data['user_name'],
                "name":data['name'],
                "last_name": data['last_name'],
                "social_network_id":data['social_network_id'],
        }
        return save_new_user(data=user)
        
        # return save_new_command(data=data)
