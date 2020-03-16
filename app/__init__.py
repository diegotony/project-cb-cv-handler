from flask import Blueprint
from flask_restplus import Api

from .main.controllers.interaction_controller import api as interaction_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(interaction_ns, path='/interaction')