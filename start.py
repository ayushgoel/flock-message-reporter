from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
import events

app = Flask(__name__)

@app.route("/events", methods=['GET', 'POST'])
def eventsRoute():
    if request.method == 'POST':
        name = request.json["name"]
        if name == "app.install":
            events.handle_app_install(request)
        if name == "app.uninstall":
            events.handle_app_uninstall(request)
        if name == "client.messageAction":
            events.handle_message_action(request)
    return ""

@app.route("/UID/<UID>")
def UIDRoute(UID):
    details = events.messageDetailsForUID(UID)
    if details:
        print details
        print "Returning details ", details.__class__
        return jsonify(details)
    abort(404)

@app.route("/configure")
def configureRoute():
    return "Configuration called!"

@app.route("/")
def baseRoute():
    return "Hello!"

if __name__ == "__main__":
    print "Starting app"
    app.run()
