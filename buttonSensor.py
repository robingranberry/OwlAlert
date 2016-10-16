import pycurl, json
from StringIO import StringIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

appID = "58027b3da4c48af6bbddc5ab"

appSecret = "65a7c99cf3e7a0f41c6c422eb3ae19a5"

pushEvent = "OwlAlert"

appID2 = "58029e2fa4c48ab9a9ddc5ab"

appSecret2 = "5c95b6c643f5785443b8c9c6ae2d0e0b"

pushEvent2 = "OwlResponse"

pushMessage = "Don't worry, be happy!"

pushMessage2 = "Owl Activated"

buffer = StringIO()

c2 = pycurl.Curl()

c2.setopt(c2.URL, 'https://api.instapush.im/v1/post')

c2.setopt(c2.HTTPHEADER, ['x-instapush-appid: ' + appID2,
'x-instapush-appsecret: ' + appSecret2,
'Content-Type: application/json'])

json_fields2 = {}

json_fields2['event']=pushEvent2
json_fields2['trackers'] = {}
json_fields2['trackers']['message']=pushMessage2

postfields2 = json.dumps(json_fields2)

c2.setopt(c2.POSTFIELDS, postfields2)

c2.setopt(c2.WRITEFUNCTION, buffer.write)

c = pycurl.Curl()

c.setopt(c.URL, 'https://api.instapush.im/v1/post')

c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
'x-instapush-appsecret: ' + appSecret,
'Content-Type: application/json'])

json_fields = {}

json_fields['event']=pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message']=pushMessage

postfields = json.dumps(json_fields)

c.setopt(c.POSTFIELDS, postfields)

c.setopt(c.WRITEFUNCTION, buffer.write)

while True:

    GPIO.wait_for_edge(16, GPIO.RISING)
    print("Button Pressed!") 
    c.perform()
    c2.perform()
    body= buffer.getvalue()
    print(body)
    buffer.truncate(0)
    buffer.seek(0)
    GPIO.wait_for_edge(16, GPIO.FALLING)
    print("Button Stopped")
          
GPIO.cleanup()

