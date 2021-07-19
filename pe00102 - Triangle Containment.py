#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:39:14 2021

@author: igorvanloo
"""

'''
Project Euler Problem 102 

We check if (0,0) is in a triangle by setting (0,0) = a + xb + yc where a,b,c are 3 co-ords of triangle
then
x = det((0,0)c) - det(ac) / det(bc)
y = det((0,0)b) - det(ab) / det(bc)

Then (0,0) is in tringle if x,y > 0 and x+y < 1

Anwser:
    228
--- 0.009732246398925781 seconds ---
    
'''

import time
import numpy as np
start_time = time.time()

def ReadFile(): #Create the inital list 
    file = open("/Users/igorvanloo/Dropbox/My Mac (Igors-MacBook-Air.local)/Desktop/Project Euler/0. Files/p102_triangles.txt")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        datalist.append([int(s) for s in x.split(',')])
    return datalist

def det(x, y):
    return x[0]*y[1] - y[0]*x[1]
    
def IsPointInTriangle(point, a, b, c):
    #Point = a + x(b-a) + y(c-a)
    v0 = a
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - a[0], c[1] - a[1])
    
    x = (det(point, v2) - det(v0, v2))/(det(v1, v2))
    y = (det(v0, v1) - det(point, v1))/(det(v1, v2))
        
    if x > 0 and y > 0 and x+y<1:
        return True
    else:
        return False
    
def compute():
    triangles = ReadFile()
    count = 0
    for i in triangles:
        if IsPointInTriangle((0,0),(i[0], i[1]),(i[2], i[3]),(i[4], i[5])) == True:
            count += 1
    return count
        

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
    
