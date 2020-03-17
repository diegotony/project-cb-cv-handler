from flask import request
from flask_restplus import Resource

from ..util.dto import CommandDto
from ..util.commands import get_all_commands, commands
from ..services.user_service import save_new_user, get_all_users,messsage_error
from ..services.interaction_service import save_new_interaction
api = CommandDto.api
_command = CommandDto.command

@api.route('/list')
class CommandList(Resource):
    @api.doc('list_of_registered_commands')
    # @api.marshal_list_with(_command, envelope='data')
    def get(self):
        """List all registered commands"""
        return get_all_commands()


@api.route('/')
class Command(Resource):
    @api.doc('list_of_registered_commands')
    def get(self):
        """List all registered commands"""
        
        return get_all_users()

    @api.response(201, 'Interaction successfully created.')
    @api.doc('create interaction with command')
    @api.expect(_command, validate=True)
    def post(self):
        """Creates a new Interaction """
        try:
            if request.json:
                data = request.json
                create_user = {
                    "user_name": data['user_name'],
                    "name": data['name'],
                    "last_name": data['last_name'],
                    "social_network_id": data['social_network_id'],
                }
                user = save_new_user(create_user)
                command = commands(data['command'])
                return command
            
        except Exception as e:
            return messsage_error("false",e)

      

        # interaction = save_new_interaction({"user":user['id'],"input_db":data['command'],"output":command})

        # return save_new_command(data=data)
