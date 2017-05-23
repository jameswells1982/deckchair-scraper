#!/usr/bin/env python

import json
import requests
queryURL = "http://api.deckchair.com/v1/camera/5833123d5e70988f7256040f/images?from=1495429200&to=1495515300"
imgURLpre = "http://api.deckchair.com/v1/viewer/image/"
imgURLpost = "?width=1920&height=1080&resizeMode=fill&gravity=Center&quality=99&format=jpg"


r = requests.get(queryURL)
data = json.loads(r.text)
if data:
    for image in data['data']:
        imageid = image['_id']
        datetime = image['taken']
        imagedata = requests.get(imgURLpre + str(imageid) + imgURLpost)
        if imagedata:
            print "saving file: " + str(datetime) + ".jpg"
            file = open(str(datetime) + ".jpg", "w")
            file.write(imagedata.content)
            file.close()
