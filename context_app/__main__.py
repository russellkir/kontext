#!/usr/bin/env python3

# stdlib imports
import json
import time
import webbrowser

# pypi imports
from flask import Flask, render_template, send_from_directory
from zoomus import ZoomClient

# local imports
from context_app import zoom

USER_ID = "MigGUNgKSFKsmATXRoB22A"

app = Flask("Kontext")


@app.route("/")
def index():
    return "Hello World"


def main():
    app.run(host="::", port=5000, threaded=True)

    print("Kontext")
    client = zoom.ZoomClient(USER_ID)
    meeting = client.create_meeting()
    # webbrowser.open(meeting["start_url"], new=2)
    # print(client.list_meetings())
    # print(client.list_live_meetings())
    print(meeting)


if __name__ == "__main__":
    main()
