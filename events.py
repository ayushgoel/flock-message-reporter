from flask import request
import redis
import config

redis_client = redis.StrictRedis(host=config.redis_config["host"], port=config.redis_config["port"])

def handle_app_install(request):
  print "Handling app install", request.json
  userID = request.json["userId"]
  token = request.json["token"]
  redis_client.set(userID, token)

def handle_app_uninstall(request):
  print "Handling app install", request.json
  userID = request.json["userId"]
  redis_client.delete(userID)
