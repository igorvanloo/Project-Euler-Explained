#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 00:31:01 2021

@author: igorvanloo
"""

'''
Project Euler Problem 630

Crossed lines

Reasoning

Given 2 sets of points (x1,y1), (x2,y2) we can create the line ax + by + c = 0
Start with y = mx + b, where m = (y2-y1)/(x2-x1) and b = y1 - mx1
then y(x2-x1) = x(y2-y1) + y1(x2-x1) - x1(y2-y1) => x(y1-y2) + y(x2-x1) + (y2x1-x2y1)

Therefore a = y1-y2, b = x2 - x1, c = y2x1-x2y1
Then we take the g = gcd(a,b), now we notice that gcd(a,b) will always divide c

Then we can describe a line by a/g, b/g, c/g

To make sure we do not produce the same line 2 different ways (a,-b,c) and (-a,b,-c)

We decide that a > 0, therefore if we encounter an a < 0 we multiply a,b,c by -1,
similarly if a = 0 and b < 0 then we multiply a,b,c by -1

Now that we are able to uniquely describe all the lines, we add them continuously to a set
to remove all duplicates, then we create a dictionary where dict[(a,b)] = number of times seen
This way we can easily keep track of the number of lines parralel to each other

if we denote the differnt slopes m1,m2,...mk

Then M = sum from 1 to k (mi) and S = sum from 1 to k of mi(M-mi)

Anwser:
(4948, 24477690)
(3109535, 9669182880384)
--- 9.037025928497314 seconds ---
'''

import time, math, eulerlib
start_time = time.time()

def LineCreator(point1,point2):
    x1, y1 = point1
    x2, y2 = point2
    
    dy = y1-y2
    dx = (x2 - x1)
    dz = -(x2*y1-x1*y2)
    temp = math.gcd(dy,dx)

    if dx < 0 or dx == 0 and dy < 0:
        dy *= -1
        dx *= -1
        dz *= -1
    return (dy/temp, dx/temp, dz/temp)

def T(pointn):
    s0 = 290797
    
    count = 0
    finallist = []
    
    while count != 2*pointn:
        sn = pow(s0,2,50515093)
        tn = (sn % 2000) - 1000
        finallist.append(tn)
        s0 = sn
        count += 1
    final = []
    
    for x in range(0,len(finallist),2):
        final.append((finallist[x], finallist[x+1]))
        
    return final
    
def compute(x):
    points = T(x)
    length = len(points)
    
    lines = set([])
    for x in range(length):
        for y in range(x+1,length):
            temp = LineCreator(points[x],points[y])
            lines.add(temp)
    M = len(lines)
    gradients = {}
    
    for a in lines:
        if (a[0],a[1]) in gradients:
            gradients[(a[0],a[1])] += 1
        else:
            gradients[(a[0],a[1])] = 1
            
    total = 0
    for b in gradients:
        total += gradients[b] * (M-gradients[b])
    
    return M, total

if __name__ == "__main__":
    print(compute(100))
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
    