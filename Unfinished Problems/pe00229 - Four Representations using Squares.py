#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:59:27 2022

@author: igorvanloo
"""
'''
Project Euler Problem 

n = a^2 + kb^2

limit > kb^2 => b < sqrt(limt/k)

Anwser:
    75373 - 10^7
--- 7.947635173797607 seconds ---

    660576 - 10^8
--- 94.26800894737244 seconds ---

    I believe I can get the answer in around an hour or two, unless there is memory overflow
'''
import time, math
start_time = time.time()

def compute(limit):
    set1 = set()
    set2 = set()
    set3 = set()
    set7 = set()
    
    for k in [1,2,3,7]:
        print(k)
        for b in range(1, int(math.sqrt(limit/k)) + 1):
            bvalue = k*b*b
            if k == 1:
                t = b
            else:
                t = 1
            for a in range(t, int(math.sqrt(limit - bvalue)) + 1):
                key = a*a + bvalue
                if key < limit:
                    if k == 1:
                        set1.add(key)
                    elif k == 2:
                        set2.add(key)
                    elif k == 3:
                        set3.add(key)
                    elif k == 7:
                        set7.add(key)
                else:
                    break
    return len(set1.intersection(set2.intersection(set3.intersection(set7))))

if __name__ == "__main__":
    print(compute(10**5))
    print("--- %s seconds ---" % (time.time() - start_time))
