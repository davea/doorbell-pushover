#!/usr/bin/env python3
import os

import requests

def callback(topic, payload):
    binary_topics = set(os.getenv("PUSHOVER_BINARY_TOPICS", "").split(","))
    if not (payload == b"ON" or topic in binary_topics):
        return
    files = None
    if topic in binary_topics:
        files = {
            "attachment": ("image.jpeg", payload)
        }
    elif os.environ.get("DOORBELL_CAMERA_URL"):
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
