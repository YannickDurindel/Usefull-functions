# This code is freaking usefull !! The this is that I wanted to make a code that loops with a whie True, and each lap is exactly n seconds
# The problem was that i couldn't just use a time.sleep(n), because the code actully take time to run, espacially mine, so here it is, it does the job well
# You juste have to define t0 = time.time() at the start of the lap, and execute the function at the end.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:04:52 2022

@author: yannick
"""

import time

def HoldOn(t0,dt):
    t1 = time.time()
    print(t0)
    print(t1)
    while t0 + dt > t1 :
        t1 = time.time()

t0 = time.time()
time.sleep(2)
HoldOn(t0,1)
print("succed")
