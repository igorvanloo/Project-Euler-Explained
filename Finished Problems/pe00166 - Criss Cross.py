#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:41:26 2022

@author: igorvanloo
"""
'''
Project Euler Problem 166

a b c d
e f g h
i j k l
m n o p

We have 16 variables therefore 10^16 possibilities we want to minimise this

Let a + b + c + d = s, 
now we want to minimize number of variables used

simple way is to notice
s - a - e - i = m 
s - b - f - j = n 
s - c - g - k = o 

s - e - f - g = h 
s - i - j - k = l 
s - a - f - k = p 

and we can notice g = s - d - j - m

Using this we only need 9 variables (a, b, c, d, e, f, i, j, k)

Anwser:
    7130034
--- 112.5133728981018 seconds ---
'''
import time
start_time = time.time()

def valid(n):
    if n < 0 or n > 9:
        return False
    return True

def compute():
    total = 0
    for a in range(0, 10):
        print(a)
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    s = a + b + c + d
                    
                    for e in range(0, 10):
                        for i in range(0, 10):
                            m = s - a - e - i
                            if valid(m):
                                for j in range(0, 10):
                                    g = s - d - j - m
                                    if valid(g):
                                        
                                        for f in range(0, 10):
                                            n = s - b - f - j
                                            if valid(n):
                                                
                                                for k in range(0, 10):
                                                    o = s - c - g - k
                                                    if valid(o):
                                                        h = s - e - f - g
                                                        if valid(h):
                                                            
                                                            l = s - i - j - k
                                                            if valid(l):
                                                                
                                                                p = s - a - f - k
                                                                if valid(p):
                                                        
                                                                    if m + n + o + p == s and d + h + l + p == s:
                                                                        '''print(total)
                                                                        print(a, b, c, d)
                                                                        print(e, f, g, h)
                                                                        print(i, j, k, l)
                                                                        print(m, n, o, p)'''
                                                                        total += 1
    
    return total
                                
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
