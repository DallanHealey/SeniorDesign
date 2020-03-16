import json
import os

import smtplib

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

#sendMail("Testing", "Woo\nTesting 123...")

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

#sendMail1()


def gyroTripped():
    print("Gro Tripped")

    # If Gyro is tripped, send email

def sensorTripped():
    print("Sensor Tripped")

    # If Sensor tripped, send email