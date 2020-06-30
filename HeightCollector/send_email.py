#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:15:04 2020

@author: tianlu
"""

from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    from_email = "helloluckytea@gmail.com"
    from_password = "********"
    to_email = email
    subject = "height data"
    message = "Your height is <strong>%s</strong> . Average height of all %s is %s." % (height,count,average_height)
    
    msg = MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    
    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
    
     
    
    