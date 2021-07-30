#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:18:32 2021

@author: igorvanloo
"""

'''
Project Euler Problem 91

A = (0,0) B = (x1, x2) C = (y1, y2)

Choose point B and C randomly, then 
AB = sqrt(x1^2 + x2^2)
AC = sqrt(y1^2 + y2^2)
BC = sqrt((x1-y1)^2 + (x2-y2)^2)

then if (maximum(AB, AC, BC))^2 = other 2 squared then this forms a right angle triangle

then we go through each point which would be ~ 6,760,000 combinations

I omit sqrt because of precision error and if x > y > 0 => x^2 > y^2

Anwser:
    
'''

import time

def right_angle_checker(B, C):
    AB = (B[0]**2 + B[1]**2)
    AC = (C[0]**2 + C[1]**2)
    BC = (B[0] - C[0])**2 + (B[1] - C[1])**2
    
    if BC > AB and BC > AC:
        if BC == AB + AC:
            return True
    elif AB > BC and AB > AC:
        if AB == BC + AC:
            return True
    elif AC > AB and AC > BC:
        if AC == AB + BC:
            return True
    return False
    
def compute(limit):
    
    points = [(x, y) for y in range(0,limit+1) for x in range(0,limit+1)]
    points.pop(0)
    
    count = 0
    for B in range(len(points)):
        for C in range(B+1, len(points)):
            if right_angle_checker(points[B], points[C]):
                #print(points[B], points[C])
                count += 1
    return count

if __name__ == "__main__":
    start_time = time.time()
    print(compute(50))
    print("--- %s seconds ---" % (time.time() - start_time))