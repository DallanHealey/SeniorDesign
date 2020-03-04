Install ssmtp
Copy ssmtp.conf to /etc/ssmtp/

Have a mail.txt file that follows the following format:
    
    To: dallan.healey@live.com
    Subject: Testing Pool Stuffs

    Testing 123...

    Wooo,
    Pool Safety

Send mail with `ssmtp <Email to deliver to> < mail.txt`
