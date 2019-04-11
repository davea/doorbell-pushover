#!/usr/bin/env python3
import os

import requests

def callback(topic, payload):
    if payload == b"ON":
        requests.post("https://api.pushover.net/1/messages.json", {
            'token': os.environ['PUSHOVER_APP_TOKEN'],
            'user': os.environ['PUSHOVER_USER_TOKEN'],
            'message': os.environ.get("PUSHOVER_MESSAGE", "Someone is at the door!"),
            'sound': os.environ.get("PUSHOVER_SOUND", "persistent"),
        })
