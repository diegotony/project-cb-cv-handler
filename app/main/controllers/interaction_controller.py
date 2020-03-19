from flask import request
from flask_restplus import Resource

from ..util.dto import InteractionDto
from ..services.interaction_service import *
from ..util.utils import array_interaccions
api = InteractionDto.api


@api.route('/')
class InteractionList(Resource):
    @api.doc('list_of_registered_interactions')
    def get(self):
        """List all registered interactions"""
        data =get_all_interactions()
        array = array_interaccions(data)

        return array
        # return 


