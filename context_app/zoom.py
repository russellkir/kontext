import logging
import requests

from context_app.http import try_post

API_KEY = "d-O8SB-JQ76esEky1qs0OQ"
API_SECRET = "TqxqygO5akXhzlD4LVrRQBYRUBwL3TSAAeho"


class ZoomClient(object):
    def __init__(self, user_id):
        self._user_id = user_id

    def create_meeting(self):
        url = "https://api.zoom.us/v1/meeting/create"
        payload = {
            "api_key": API_KEY,
            "api_secret": API_SECRET,
            "host_id": self._user_id,
            "type": 1,
            "topic": "TEST",
        }
        return try_post(url=url, json=payload)

    def list_meetings(self):
        url = "https://api.zoom.us/v1/meeting/list"
        payload = {
            "api_key": API_KEY,
            "api_secret": API_SECRET,
            "host_id": self._user_id,
        }
        return try_post(url=url, json=payload)

    def list_live_meetings(self):
        url = "https://api.zoom.us/v1/meeting/live"
        payload = {
            "api_key": API_KEY,
            "api_secret": API_SECRET,
        }
        return try_post(url=url, json=payload)
