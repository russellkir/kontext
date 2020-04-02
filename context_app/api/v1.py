#!/usr/bin/python3

import json
from flask import abort
from flask_restplus import fields, Namespace, Resource


api = Namespace("kontext", description="Kontext App")

test_model = api.model("Test", {"test": fields.Boolean})


@api.route("/test")
class Test(Resource):
    @api.doc("Test API")
    @api.response(404, "test not found")
    @api.marshal_with(test_model)
    def get(self):
        return {"test": True}, 200
