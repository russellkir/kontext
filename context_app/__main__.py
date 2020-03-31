#!/usr/bin/env python3

# stdlib imports
import json
import time
import webbrowser
from zoomus import ZoomClient

# local imports
from context_app import zoom

USER_ID = "MigGUNgKSFKsmATXRoB22A"


def main():
    print("Kontext")
    client = zoom.ZoomClient(USER_ID)
    # meeting = client.create_meeting()
    # webbrowser.open(meeting["start_url"], new=2)
    print(client.list_meetings())
    print(client.list_live_meetings())


if __name__ == "__main__":
    main()
