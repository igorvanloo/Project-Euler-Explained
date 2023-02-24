# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:49:50 2023

@author: igorvanloo
"""
'''
Project Euler Problem 816

simple closest points algorithm O(n*log^2(n)), optimsed to O(n*log(n))
I took a programming class this semester and we actually briefly talked about this algorithm

Anwser:
    20.880613018
--- 70.80705571174622 seconds ---
'''

import time, math
start_time = time.time()

def distance(x, y):
    x1, x2 = x
    y1, y2 = y
    return math.sqrt(pow(y1-x1,2) + pow(y2-x2,2))
    
def pointsGen(n):
    s0 = 290797
    points = []
    for x in range(2*n - 1):
        s1 = ((s0*s0) % 50515093)
        if x % 2 == 0:
            P = (s0, s1)
            points.append(P)
        s0 = s1
    return points

def bruteForce(points):
    minDist = None
    for i in range(len(points)):
        x = points[i]
        for j in range(i + 1, len(points)):
            y = points[j]
            currDist = distance(x, y)
            if minDist == None:
                minDist = currDist
            if currDist < minDist:
                minDist = currDist
    return minDist

def closestPairOfPointsSlow(points):
    #O(nlog^2(n)) solution
    l = len(points)
    if l <= 3:
        return bruteForce(points)
    
    mid = l//2
    #Find the line x that splits the plane in 2
    xmid = (points[mid - 1][0] + points[mid][0])/2
    
    #Find the minimum distance in the left and right side, and return the min of those 2
    d = min(closestPairOfPointsSlow(points[:mid]), closestPairOfPointsSlow(points[mid:]))
    
    #Make the left and right strips of distance d away from xmid
    left = [x for x in points[:mid] if xmid - d < x[0] < xmid]
    right = [x for x in points[mid:] if xmid <= x[0] < xmid + d]
    
    right = sorted(right, key = lambda x : x[1])
    for p in left:
        box = [x for x in right if ((p[0] < x[0] < p[0] + d) and (p[1] - d < x[1] < p[1] + d))]
        for q in box:
            newD = distance(p, q)
            if newD < d:
                d = newD
    return d

def closestPairOfPoints(points):
    #O(nlog(n))
    l = len(points)
    if l <= 3:
        return bruteForce(points), sorted(points)
    
    mid = l//2
    #Find the line x that splits the plane in 2
    xmid = (points[mid - 1][0] + points[mid][0])/2
    
    #Find the minimum distance in the left and right side, and return the min of those 2
    dLeft, pointsLeft = closestPairOfPoints(points[:mid])
    dRight, pointsRight = closestPairOfPoints(points[mid:])
    
    #Sort the points
    points = pointsLeft + pointsRight
    
    d = min(dLeft, dRight)
    
    #Make the left and right strips of distance d away from xmid
    left = []
    right = []
    for x in points:
        if xmid - d < x[0] < xmid:
            left.append(x)
        elif xmid <= x[0] < xmid + d:
            right.append(x)
        elif x[0] >= xmid + d:
            break
    
    for p in left:
        box = [x for x in right if ((p[0] < x[0] < p[0] + d) and (p[1] - d < x[1] < p[1] + d))]
        for q in box:
            newD = distance(p, q)
            if newD < d:
                d = newD
    return d, points

def d(k):
    points = sorted(pointsGen(k))
    return round(closestPairOfPoints(points)[0], 9)

if __name__ == "__main__":
    print(d(2*10**5))
    print("--- %s seconds ---" % (time.time() - start_time))
