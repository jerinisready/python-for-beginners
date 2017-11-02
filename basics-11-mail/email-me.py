#!/usr/bin/python

import smtplib

sender = 'from@fromdomain.com'
receivers = ['topersorn1@todomain.com','topersorn2@todomain.com',]

message = """From: From Person <%s>
To: To Person <%s>
Subject: SMTP e-mail test

This is a test e-mail message.
""" % (sender, '>, <'.join(receievers))

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
