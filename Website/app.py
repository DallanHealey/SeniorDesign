from flask import Flask, render_template, jsonify, request
from forms import UserSettings
from datetime import datetime
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'l33tKey'

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

# Settings Page
# Loads and modifies previous settings to match current settings. File is stored back a directory (../)
@app.route("/settings", methods=['GET', 'POST'])
def settings():
    email = ""
    phone = ""

    try:
        os.chdir("..")
        with open('settings.json', 'r') as fp:
            json_info = json.load(fp)    
            email = json_info[1]['email']
            phone = json_info[1]['phone']
    except:
        pass
    os.chdir("Website")

    form = UserSettings()

    if form.is_submitted():
        result = request.form
        result = [*result.values()]
        email = result[0]
        phone = result[1]
        json_settings = ["info", {"email": email, "phone": phone}]
        os.chdir("..")
        try:
            with open('settings.json', 'w') as fp:
                json.dump(json_settings, fp)
        except:
            pass
        os.chdir("Website")

    return render_template("settings.html", form=form, email=email, phone=phone)