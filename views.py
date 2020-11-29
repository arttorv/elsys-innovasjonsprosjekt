from django.shortcuts import render
from django.shortcuts import redirect
import requests
import json
import threading
import time

loraURL = 'https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/innovasjonsprosjekt7/swingbro?key=ttn-account-v2.N6AA0zYmlh0GW1XghgjE0mjIkeX1tfC11WI5SHPMVCw'
pipeURL = 'https://0a6deea4061ec0559534eb99241ca9ec.m.pipedream.net'
loraJson = {
    "dev_id": "innovationproj",
    "port": 1,
    "confirmed": True,
    "payload_fields": {
        "status": ""
    }
}

def state(stat, request):
    while True:
        get = requests.get(pipeURL).json()
        last = get["status"]
        loraJson["payload_fields"]["status"] = last
        if last != stat:
            requests.post(loraURL, data=json.dumps(loraJson))
            return index(request)
        else: 
            time.sleep(30) 

def index(request):
    
    get = requests.get(pipeURL).json()
    last = get["status"]
    loraJson["payload_fields"]["status"] = last
    
    x = threading.Thread(target=state, args=[last, request])
    x.setDaemon(False)
    x.start()

    context = {"status" : last}
    return render(request, "elsysapp/index.html", context)



