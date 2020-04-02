#!/usr/bin/env python3

# stdlib imports
import os
import json
import time
import webbrowser

# pypi imports
from flask import Flask, render_template, send_from_directory
from zoomus import ZoomClient

# local imports
from context_app import zoom
from context_app.api import blueprint as api

USER_ID = "MigGUNgKSFKsmATXRoB22A"

app = Flask("context_app", template_folder="templates")
app.register_blueprint(api)


@app.route("/")
def index():
    return render_template("index.html.tmpl")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.png",
        mimetype="image/png",
    )


def main():
    app.run(host="::", port=5000, debug=False, threaded=True)

    print("Kontext")
    # client = zoom.ZoomClient(USER_ID)
    # meeting = client.create_meeting()
    # webbrowser.open(meeting["start_url"], new=2)
    # print(client.list_meetings())
    # print(client.list_live_meetings())
    # print(meeting)


if __name__ == "__main__":
    main()
