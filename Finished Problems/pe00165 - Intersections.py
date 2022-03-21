#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:22:40 2022

@author: igorvanloo
"""

'''
Project Euler Problem 165

Anwser:
    2868868
--- 38.95456790924072 seconds ---
'''

import time, math
start_time = time.time()

def T(num_points):
    s0 = 290797
    finallist = []
    for x in range(4*num_points):
        sn = pow(s0,2,50515093)
        tn = sn % 500
        finallist.append(tn)
        s0 = sn
    final = []
    for x in range(0,len(finallist),4):
        final.append((finallist[x], finallist[x+1], finallist[x+2], finallist[x+3]))
    return final

def LineCreator(point1, point2):
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

def interesect(segment1, segment2):
    x1, y1, x2, y2 = segment1
    x3, y3, x4, y4 = segment2
    A1, B1, C1 = LineCreator((x1, y1), (x2, y2))
    A2, B2, C2 = LineCreator((x3, y3), (x4, y4))
    C1, C2 = -C1, -C2
    #print(A1, B1, C1)
    #print(A2, B2, C2)
    det = A1 * B2 - A2 * B1
    if (det == 0):
      #print("lines are parallel")
      return False
    else:
      x = (B2 * C1 - B1 * C2) / det
      y = (A1 * C2 - A2 * C1) / det
      #print(x, y)
      
      if (min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)) and (min(x3, x4) <= x <= max(x3, x4)) and (min(y3, y4) <= y <= max(y3, y4)):
          if (x, y) == (x1, y1) or (x, y) == (x2, y2) or (x, y) == (x3, y3) or (x, y) == (x4, y4):
              return False
          else:
              return (x, y)
      else:
          return False
    
def compute(n):
    segments = T(n)
    #segments = ([27, 44, 12, 32], [46, 53, 17, 62], [46, 70, 22, 40])
    #print(segments)
    true_points = set()
    for x in range(len(segments)):
        if x % 1000 == 0:
            print(x)
        for y in range(x+1, len(segments)):
            point = interesect(segments[x], segments[y])
            #print(segments[x], segments[y], point)
            if point != False:
                true_points.add(point)
    return len(true_points)
    
if __name__ == "__main__":
    print(compute(5000))
    print("--- %s seconds ---" % (time.time() - start_time))