#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:00:17 2022

@author: igorvanloo
"""
'''
Project Euler Problem 277

a_{n+1} = a_n/3 if 0 = a_n mod 3 denoted as D
a_{n+1} = (4a_n + 2)/3 if 1 = a_n mod 3 denoted as U
a_{n+1} = (2a_n - 1)/3 if 2 = a_n mod 3 denoted as d

Anwser: 
    1125977393124310
--- 0.0007550716400146484 seconds ---
'''
import time
start_time = time.time()

def seq_finder(num, mask, count):
    if mask == "":
        return count
    elif mask[0] == "D":
        if num % 3 == 0:
            return seq_finder(num//3 , mask[1:], count + 1)
        else:
            return count
    elif mask[0] == "U":
        if num % 3 == 1:
            return seq_finder((4*num + 2)//3 , mask[1:], count + 1)
        else:
            return count
    elif mask[0] == "d":
        if num % 3 == 2:
            return seq_finder((2*num - 1)//3 , mask[1:], count + 1)
        else:
            return count
    
def compute(limit, seq):
    first_move = seq[0]
    for x in [limit, limit + 1, limit + 2]:
        if first_move == "D":
            if x % 3 == 0:
                start = x
        elif first_move == "U":
            if x % 3 == 1:
                start = x
        elif first_move == "d":
            if x % 3 == 2:
                start = x
    
    step = 3
    max_count = 1
    while True:
        print(start)
        t = seq_finder(start, seq, 0)
        if t == len(seq):
            return start
        max_count = max(max_count, t) 
        start += pow(step, max_count)


if __name__ == "__main__":
    print(compute(10**6, 'DdDddUUdDD'))
    print(compute(10**15, 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'))
    print("--- %s seconds ---" % (time.time() - start_time))
