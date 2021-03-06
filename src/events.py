from flask import request
import redis
import config
import datetime
import json

redis_client = redis.StrictRedis(host=config.redis_config["host"], port=config.redis_config["port"])

def handle_app_install(request):
    print "Handling app install", request.json
    userID = request.json["userId"]
    token = request.json["token"]
    redis_client.set(userID, token)

def handle_app_uninstall(request):
    print "Handling app uninstall", request.json
    userID = request.json["userId"]
    redis_client.delete(userID)

def date_key():
    return "{}-{:02d}".format(datetime.date.today().year, datetime.date.today().month)

def add_report_time(response):
    response["reportTime"] = datetime.datetime.today().isoformat()
    return response

def handle_message_action(request):
    print "Handling message action", request.json
    messagesUIDs = request.json["messageUids"]
    for messageUID in messagesUIDs:
        if not redis_client.exists(messageUID):
            print "Saving UID", messageUID
            key = date_key()
            redis_client.rpush(key, messageUID)
            redis_client.set(messageUID, json.dumps(add_report_time(request.json)))
        else:
            print "Ignoring UID", messageUID

def messageDetailsForUID(UID):
    if redis_client.exists(UID):
        details = redis_client.get(UID)
        print "Got UID", UID, details
        return json.loads(details)
    return None

def UIDsForMonth(month):
    if redis_client.exists(month):
        details = redis_client.lrange(month, 0, -1)
        print "Got UID", month, details
        return details
    return None
