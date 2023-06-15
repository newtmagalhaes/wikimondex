from flask import Blueprint
from flask_restx import Api

# import namespaces
from .especie import api as especie_ns
from .bolsista import api as bolsista_ns
from .especime import api as especime_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='API',
    version='1.0'
)

# add namespaces
api.add_namespace(especie_ns)
api.add_namespace(bolsista_ns)
api.add_namespace(especime_ns)