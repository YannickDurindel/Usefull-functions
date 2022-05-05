# I didn't create this function, this is a casual one that I personally use when I run a code on a different machine than mine, so that I could eventually check regulay the evolution of my code by mail !!!

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:21:29 2022

@author: yannick
"""

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sender.address@email.com"  # Enter your address
receiver_email = "reciever.address@email.com"  # Enter receiver address
password = "your password"  #enter your mail box's password
message = """\
Subject: Feedback from any code you want!

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
