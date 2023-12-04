#!/usr/local/bin/python3

import json
from websockets.sync.client import connect

token = "TOKEN" # your personal token
site = "SITEID" # your site's ID

url = "wss://dash.iiwari.cloud/api/v1/sites/"+site+"/stream?filter=kalman&token="+token

with connect(url) as websocket:
    while True:
        ev = websocket.recv()
        print(json.loads(ev))
