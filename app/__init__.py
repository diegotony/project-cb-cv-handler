from flask import Blueprint
from flask_restplus import Api

from .main.controllers.interaction_controller import api as interaction_ns
from .main.controllers.command_controller import api as command_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CHANNEL HANDLER FLASK RESTPLUS API',
          version='1.0',
          description='channel handler'
          )

# api.add_namespace(interaction_ns, path='/interaction')
api.add_namespace(command_ns, path='/command')
