# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 00:37:09 2023

@author: igorvanloo
"""
'''
Project Euler Problem 761

Anwser:
    5.05505046
--- 0.01566624641418457 seconds ---
'''
import time
from sympy import sin, cos, tan, pi, acos
start_time = time.time()
    
def compute(n):
    K = 0
    theta = pi/n
    f = lambda k : sin(k*theta) - (k + n)*tan(theta)*cos(k*theta)
    
    while f(K) < 0:
        K += 1
    K -= 1
    a = (K*theta + acos(2*sin(K*theta)/((K + n)*tan(theta)) -cos(K*theta)))/2
    return round(1/cos(a), 8)

if __name__ == "__main__":
    print(compute(6))
    print("--- %s seconds ---" % (time.time() - start_time))
