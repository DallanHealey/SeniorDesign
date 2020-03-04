import os

# Basically, if something happens, we can do os.system() with that command and send the email. The email would be pulled from the settings page on the website.
while (1):
    a = '0'
    a = input("Enter a 0 or 1")

    if a == '1':
        os.system("ssmtp dallan.healey@live.com < ../Mail/mail.txt")