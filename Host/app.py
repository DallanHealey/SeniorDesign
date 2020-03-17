import json
import os
import datetime

import smtplib

ID = 0

def sendMail(subject, message):
    email = ""
    try:
        os.chdir("..")
        with open('settings.json', 'r') as fp:
            json_info = json.load(fp)    
            email = json_info[1]['email']
    except:
        pass
    os.chdir("Host/")

    if (email == ""):
        print("No email configured")
    else:
        mail = open("mail.txt", "w")
        mail.write("To: {0}\n".format(email))
        mail.write("Subject: {0}\n".format(subject))
        mail.write("\n")
        mail.write(message)
        mail.write("\n\n")
        mail.write("Wooo,\n")
        mail.write("Pool Safety Team")

        command = "ssmtp {0} < mail.txt".format(email)
        #return_value = os.system(command)

        '''
        if (return_value != 0):
            print("Error sending mail to ", email)
        else:
            print("Email sent to ", email)
        '''

# Pretty sure this works better than the above sendMail function
def sendMail1():
    sender = 'poolsafetyelec4000@gmail.com'
    receivers = ['dallan.healey@live.com']

    message = """From: Pool Safety <poolsafetyelec4000@gmail.com>
    To: To Person <dallan.healey@live.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 25)
        smtpObj.starttls()
        smtpObj.login("poolsafetyelec4000@gmail.com", "JMjU3By38gXsZKuy")
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")


def makeNotification(message, time, typeOfNotification):
    ID = 1
    os.chdir("..")
    json_notification = ""
    if os.path.isfile("notifications.json") != False:
        # Read in current data
        notifications = open("notifications.json", "r")
        json_notification = json.load(notifications)
        
        # Get oldest ID
        ID = int(json_notification[-1]["id"]) + 1
        json_notification = json.dumps(json_notification).strip("]")
        
        # Delete the file so we can make a new clean one
        notifications.close()
        os.remove("notifications.json")

    # Create a new file
    notifications = open("notifications.json", "w+")

    new_json = json.dumps([{"id": ID, "message": message, "time": time, "type": typeOfNotification}])
    if (ID != 1):
        new_json = new_json.strip("[")
        new_json = ", " + new_json
    json_notification = (json_notification if ID != 1 else "") + new_json
    json_notification = json.loads(json_notification)
    json.dump(json_notification, notifications)
    notifications.close()
    os.chdir("Host")

def gyroTripped():
    print("Gyro Tripped")
    makeNotification("Gyro has been tripped", str(datetime.datetime.now()), "gyro")
    # If Gyro is tripped, send email

def sensorTripped():
    print("Sensor Tripped")
    makeNotification("Sensor has been tripped", str(datetime.datetime.now()), "sensor")
    # If Sensor tripped, send email

def voltageTripped():
    print("Voltage Tripped")
    makeNotification("Voltage has been tripped", str(datetime.datetime.now()), "voltage")
    # If Voltage tripped, send email

while (True):
    a = input("")
    if a == '1':
        gyroTripped()
    if a == '2':
        sensorTripped()
    if a == 'q':
        break