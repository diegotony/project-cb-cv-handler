from flask import request
from flask_restplus import Resource

from ..util.dto import InteractionDto
from ..services.interaction_service import *

api = InteractionDto.api
_interaction = InteractionDto.interaction


@api.route('/')
class InteractionList(Resource):
    @api.doc('list_of_registered_interactions')
    @api.marshal_list_with(_interaction, envelope='data')
    def get(self):
        """List all registered interactions"""
        return get_all_interactions()

    # @api.response(201, 'Interaction successfully created.')
    # @api.doc('create a new interaction')
    # @api.expect(_interaction, validate=True)
    # def post(self):
    #     """Creates a new Interaction """
    #     data = request.json
    #     return save_new_interaction(data=data)

