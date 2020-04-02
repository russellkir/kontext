#!/usr/bin/python3

import json
import webbrowser
import requests
from flask import abort
from flask_restplus import fields, Namespace, Resource

from zoomus import ZoomClient
from context_app import zoom

api = Namespace("kontext", description="Kontext App")

zoom_model = api.model("Zoom", {"zoom": fields.String})


@api.route("/zoom")
class Zoom(Resource):
    @api.doc("Launch zoom meeting")
    @api.expect(zoom_model)
    @api.response(201, "Zoom username valid")
    @api.marshal_with(zoom_model, code=201)
    def post(self):
        try:
            client = zoom.ZoomClient(api.payload["zoom"])
            meeting = client.create_meeting()
            webbrowser.open(meeting["start_url"])
            r = requests.post(url="http://localhost:5000/create_redirect", data=meeting)
            return {"zoom": True}, 200
        except:
            abort(400, "Unable to launch zoom meeting")
