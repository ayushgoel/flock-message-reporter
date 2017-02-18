from flask import Flask
from flask import request
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
    return ""

@app.route("/status")
def statusRoute():
    return "Up"

@app.route("/configure")
def configureRoute():
    return "Configuration called!"

@app.route("/")
def baseRoute():
    return "Hello!"

if __name__ == "__main__":
    print "Starting app"
    app.run()
