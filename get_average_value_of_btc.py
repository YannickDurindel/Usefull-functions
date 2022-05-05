# I found out by expirience that this code version isn't very accurate, you better use an API on a broker site to be more precise

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:07:45 2021

@author: yannick
"""

import requests
import time

btc = 0
btc_val = []
btc_irt = []
n = 0

while n<5 :
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc = data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13]
    btc = int(btc)*0.0001
    btc_irt.append(btc)
    time.sleep(1)
    n+=1

btc_val.append((btc_irt[0]+btc_irt[1]+btc_irt[2]+btc_irt[3]+btc_irt[4])/5)

print(btc_val)
