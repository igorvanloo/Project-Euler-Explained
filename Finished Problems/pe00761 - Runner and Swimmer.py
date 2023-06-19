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

def find_K(n):
    theta = pi/n
    K = lambda k : sin(k*theta) - (k + n)*tan(theta)*cos(k*theta)
    
    for k in range(n + 1):
        if K(k) < 0 < K(k + 1):
            return k

def find_a(n):
    K = find_K(n)
    theta = pi/n
    return (K*theta + acos(2*sin(K*theta)/((K + n)*tan(theta)) -cos(K*theta)))/2
    
def compute(n):
    a = find_a(n)
    return round(1/cos(a), 8)

if __name__ == "__main__":
    print(compute(6))
    print("--- %s seconds ---" % (time.time() - start_time))
