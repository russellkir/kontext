#!/usr/bin/env python3

# stdlib imports
import os
import json
import time
import webbrowser
import urllib.parse as urlparse
from urllib.parse import parse_qs

# pypi imports
from flask import Flask, render_template, send_from_directory, redirect, url_for, request
from flask_cors import CORS
from zoomus import ZoomClient

# local imports
from context_app import zoom
from context_app.api import blueprint as api

USER_ID = "MigGUNgKSFKsmATXRoB22A"
existing_rooms = []

app = Flask("context_app", template_folder="templates")
app.register_blueprint(api)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", existing_rooms = existing_rooms)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.png",
        mimetype="image/png",
    )

@app.route("/create_redirect", methods=["POST"])
def redirect():
    try:
        parsed_body = urlparse.urlparse(request.get_data().decode())
        join_url = parse_qs(parsed_body.path)['join_url'][0]
        existing_rooms.append(join_url)
        # print(url_for('index'))
        return {}, 200
    except:
        return {}, 400

if __name__ == "__main__":
    app.run(host="::", port=5000, debug=False, threaded=True)

    print("Kontext")
    # client = zoom.ZoomClient(USER_ID)
    # meeting = client.create_meeting()
    # webbrowser.open(meeting["start_url"], new=2)
    # print(client.list_meetings())
    # print(client.list_live_meetings())
    # print(meeting)
    main()
