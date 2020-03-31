import json
from zoomus import ZoomClient

API_KEY="d-O8SB-JQ76esEky1qs0OQ"
API_SECRET="TqxqygO5akXhzlD4LVrRQBYRUBwL3TSAAeho"
CREATE_MEETING_URI="https://api.zoom.us/v1/meeting/create"
HOSE_ID="MigGUNgKSFKsmATXRoB22A"

def main():
    print("Kontext")
    zoom_client = ZoomClient(API_KEY, API_SECRET)
    user_list_response = zoom_client.user.list()
    user_list = json.loads(user_list_response.content)

    print(user_list["users"][0]["first_name"])
    # zoom_client.meeting.create()

if __name__ == "__main__":
    main()
