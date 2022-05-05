# Function that plots the btc curve in real time !

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:01:31 2022

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001

def HoldOn(t0,dt):
    t1 = time.time()
    while t0 + dt > t1 :
        t1 = time.time()
        
def curve (x,y,title,yname):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel(yname)
    plt.title(title)
    plt.show()
    
t = []
btc_val = []
while True :
    try :
        t0 = time.time()
        t.append(t0)
        btc_val.append(getbitcoin())
        curve(t,btc_val,"bitcoin curve ",'bitcoin value (EUR)')
        HoldOn(t0,1)
    except KeyboardInterrupt:
        print('algo ended')
        print('total time = ',len(t)+1,'sec')
        print('average bitcoin value = ',sum(btc_val)/(len(btc_val)+1),'EUR')
        break
