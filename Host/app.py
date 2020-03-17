import json
import os
import datetime

# Sends mail to user
# This mail function does not work properly. Running the command in the actual terminal works properly.
def sendMail(subject, message):
    email = ""
    sendEmail = '0'
    try:
        os.chdir("..")
        with open('settings.json', 'r') as fp:
            json_info = json.load(fp)    
            email = json_info[1]['email']
            sendEmail = json_info[1]['sendEmail']
    except:
        pass
    os.chdir("Host/")


    if (email == ""):
        print("No email configured")
    elif (sendEmail != '1'):
        print("Email not sent due to user config")
        return
    else:
        mail = open("mail.txt", "w")
        mail.write("To: {0}\n".format(email))
        mail.write("Subject: {0}\n".format(subject))
        mail.write("\n")
        mail.write(message)
        mail.write("\n\n")
        mail.write("Pool Safety Team")

        command = "ssmtp {0} < mail.txt".format(email)
        #return_value = os.system(command)
        '''
        if (return_value != 0):
            print("Error sending mail to ", email)
        else:
            print("Email sent to ", email)
        '''

# Takes image of the pool when desired
# Will happen anytime a sensor is tripped    
def takeImage():
    pass

# Makes a JSON notification and essentially appends it to notifications.json
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
    takeImage()
    makeNotification("Gyro has been tripped", str(datetime.datetime.now()), "gyro")
    
    # If Gyro is tripped, send email
    sendMail("Pool Event", "Waves have been detected in the pool.")

def sensorTripped():
    print("Sensor Tripped")
    takeImage()
    makeNotification("Sensor has been tripped", str(datetime.datetime.now()), "sensor")
    
    # If Sensor tripped, send email
    sendMail("Pool Event", "The pressure has changed in the pool.")

def voltageTripped():
    print("Voltage Tripped")
    takeImage()
    makeNotification("Voltage has been tripped", str(datetime.datetime.now()), "voltage")
    
    # If Voltage tripped, send email
    sendMail("Pool Event", "Voltage has been detected in the pool.")


# This simulates events happening
while (True):
    a = input("1 for Gyro, 2 for Sensor, 3 for Voltage (q to quit): ")
    if a == '1':
        gyroTripped()
    elif a == '2':
        sensorTripped()
    elif a == '3':
        voltageTripped()
    if a == 'q':
        break