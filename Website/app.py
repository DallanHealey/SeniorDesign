from flask import Flask, render_template, jsonify, request, flash
from forms import UserSettings
from datetime import datetime
import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'l33tKey'

def loadNotifications():
    os.chdir("..")
    notifications = open("notifications.json", "r")
    notify = json.load(notifications)
    notifications.close()
    os.chdir("Website")
    return notify


# Dashboard
@app.route("/")
def index():
    return render_template("index.html", notifications=loadNotifications(), cameraFeed=[])

# This returns all the notifications, formatted for human consumption
@app.route("/notifications")
def notifications():
    return render_template("notifcations.html", id=-2, notifications=loadNotifications())

# This only returns JSON data for a REST endpoint
# /0 returns all notifications
@app.route("/notifications/<id>")
def specificNotification(id):
    notify = loadNotifications()
    max_id = notify[-1]["id"]
    if int(id) - 1 != -1 and int(max_id) >= int(id):
        return jsonify(notify[int(id) - 1])
    else:
        return jsonify(notify)

@app.route('/livefeed')
def livefeed():
    return render_template("livefeed.html")


# Settings Page
# Loads and modifies previous settings to match current settings. File is stored back a directory (../)
@app.route("/settings", methods=['GET', 'POST'])
def settings():
    email = ""
    phone = ""
    sendEmail = 1

    try:
        os.chdir("..")
        with open('settings.json', 'r') as fp:
            json_info = json.load(fp)    
            email = json_info[1]['email']
            phone = json_info[1]['phone']
            sendEmail = json_info[2]['sendEmail']
    except:
        pass
    os.chdir("Website")

    form = UserSettings()

    if form.is_submitted():
        result = request.form
        result = [*result.values()]
        email = result[0]
        phone = result[1]
        sendEmail = '1' if result[2] == 'y' else '0'
        
        if (email == "" and sendEmail == '1'):
            flash("Cannot send email if there is no provided email", "error")
            sendEmail = '0'   

        json_settings = ["info", {"email": email, "phone": phone}, "settings", {"sendEmail": sendEmail}]
        os.chdir("..")
        try:
            with open('settings.json', 'w') as fp:
                json.dump(json_settings, fp)
        except:
            pass
        os.chdir("Website")

    return render_template("settings.html", form=form, email=email, phone=phone, sendEmail=sendEmail)