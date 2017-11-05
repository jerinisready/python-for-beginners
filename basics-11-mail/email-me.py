#!/usr/bin/python
import smtplib

sender = 'jerinisready@gmail.com'
password = r'" /3uc@lyptu5/ "'
receivers = [sender,]

message = """From: PYTHONCEK HANDS-ON WORKSHOP <%s>
To: AUDIANCE  PYTHONCEK HANDS-ON WORKSHOP [s] <%s>
Subject: CEK PYTHON HANDS-ON WORKSHOP

THIS MUCH EASY TO SEND A MAIL!!
""" % (sender, '>, <'.join(receivers))

# WE HAVE TO GET CONNECTED TO A SERVER AND PORT
# login into server
# SET MODE SSL / TLS
# SEND MAIL


try:
   connection = smtplib.SMTP('smtp.gmail.com', 587)
   connection.starttls()
   connection.login(sender,password)
   connection.sendmail(sender, receivers, message)
   connection.quit()
   print "Successfully sent email"
except smtplib.SMTPException as e:
   print "Error: unable to send email\n",e


# WORRIED OF NOT SENDING FROM GMAIL ?
# TURN ON ACCESS TO LESS SECURE APPS *TEMPORARLY*
# https://myaccount.google.com/lesssecureapps?pli=1
