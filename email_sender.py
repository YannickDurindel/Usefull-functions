#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:10:30 2022

@author: yannick
NB : this is a very bold code that requires good wifi connection. 
"""

import yagmail
import time

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:19:43 2022

@author: yannick
"""

with open('/home/yannick/Documents/useless/py_codes/Email_broadcast/email_list.txt') as f:
    email = [line for line in f.readlines()]

user = 'yannick.durindel@gmail.com'
app_password = 'vavwcwykkzbmpdvw' # a token for gmail
subject = 'Can you teach your computer how to trade crypto 24/7 ?'

content = """
Can You teach your computer how to trade cryptocurrencies 24/7 ?

The answer is yes ! And guess what, you don't even need to know about trading, or coding !!!
If you want more info check this website : http://cryptobot.trading , you'll get a free insight.

Hopping you'll enjoy !
Durindel Yannick
Follow me on instagram at @student_entreprneur
"""

for k in range(96,len(email)):
    to = email[k]
    try :
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
            print('Sent email successfully   '+str(round(100*k/len(email),3))+"%")
            k+=1
    except :
        print('sending fail')