from flask import Blueprint
from flask_restplus import Api

from .v1 import api as ns1

blueprint = Blueprint("api", "Kontext app", url_prefix="/api/v1")

api = Api(
    blueprint, title="Kontext", version="0.0.1", description="Kontext API"
)

api.add_namespace(ns1)
