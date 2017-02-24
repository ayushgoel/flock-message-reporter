from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask import send_from_directory
import events

app = Flask(__name__)

@app.route("/events", methods=['POST'])
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

@app.route("/UID", methods=['POST'])
def UIDRoute():
    if request.method == 'POST':
        UID = request.json['UID']
        details = events.messageDetailsForUID(UID)
        if details:
            print details
            print "Returning details ", details.__class__
            return jsonify(details)
    abort(404)

@app.route("/history", methods=['POST'])
def historyRoute():
    if request.method == 'POST':
        print request.json
        month = request.json['month']
        UIDs = events.UIDsForMonth(month)
        if UIDs:
            print UIDs
            print "Returning UIDs ", UIDs.__class__
            return jsonify(UIDs)
    abort(404)

@app.route("/configure")
def configureRoute():
    return "Configuration called! We don't handle this yet."

@app.route("/")
def baseRoute():
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    print "Starting app"
    app.run()
