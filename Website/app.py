from flask import Flask, render_template, jsonify
from datetime import datetime
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

id = 1
string = ["notification", {"id": id, "message": "testing messages", "timestamp": "7 July 21:00:00"}]
json_string = json.dumps(string)

# Dashboard
@app.route("/")
def hello():
    notify = ['test']
    return render_template("index.html", notifications=notify, cameraFeed=[])

@app.route("/notifications")
def notifications():
    notify = json.loads(json_string)
    
    return render_template("notifcations.html", notifications=notify)

@app.route("/notifications/<id>")
def specificNotification(id):
    notify = json.loads(json_string)

    return render_template("notifcations.html", id=int(id), message=notify[int(id)]['message'])

@app.route('/livefeed')
def livefeed():
    return render_template("livefeed.html")

# Changing a from 1 to 2 will output testing1 array on website
@app.route("/testing")
def testing():
    a = 1
    testing = ["hello", "wooo"]
    testing1 = ["hello1", "wooo1"]

    return render_template('testing.html', a=a, testing=testing, testing1=testing1)