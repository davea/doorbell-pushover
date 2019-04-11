#!/usr/bin/env python3
import os

import requests

def callback(topic, payload):
    if payload == b"ON":
        files = None
        if os.environ.get("DOORBELL_CAMERA_URL"):
            try:
                files = {
                    "attachment": ("image.jpeg", requests.get(os.environ['DOORBELL_CAMERA_URL'], stream=True, timeout=5).raw)
                }
            except:
                pass
        requests.post("https://api.pushover.net/1/messages.json", {
            'token': os.environ['PUSHOVER_APP_TOKEN'],
            'user': os.environ['PUSHOVER_USER_TOKEN'],
            'message': os.environ.get("PUSHOVER_MESSAGE", "Someone is at the door!"),
            'sound': os.environ.get("PUSHOVER_SOUND", "persistent"),
        }, files=files, timeout=5)
