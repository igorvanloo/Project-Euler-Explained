# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 09:58:36 2026

@author: Igor Van Loo
"""
'''
Project Euler Problem 938

Answer:
    0.2928967987
--- 144.66587471961975 seconds ---
--- 5.404412031173706 seconds --- using PyPy
'''
import time
start_time = time.time()

def compute(R, B):
    #Create R * B array
    P = [[0 for _ in range(B + 1)] for _ in range(R + 1)]
    
    #Set initial values
    for b in range(B + 1):
        P[0][b] = 1
    for r in range(1, R + 1):
        P[r][0] = 0
    
    #Compue the entire array
    for r in range(2, R + 1, 2):
        for b in range(1, B + 1):
            t1 = r*r - r
            t2 = b*b - b
            t3 = (r + b)*(r + b - 1)
            
            c1 = t1 / t3
            c2 = 2*r*b / t3
            c3 = t2 / ((r + b)*(r + b - 1))
            
            P[r][b] = (c1 * P[r - 2][b] + c2 * P[r][b - 1]) / (1 - c3)
    return round(P[R][B], 10)

if __name__ == "__main__":
    print(compute(2*12345, 12345))
    print("--- %s seconds ---" % (time.time() - start_time))