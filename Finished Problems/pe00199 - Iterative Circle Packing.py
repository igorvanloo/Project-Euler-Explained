#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:58:33 2022

@author: igorvanloo
"""
'''
Project Euler Problem 199

Descartes Theorem: 
Given three circles with curvatures k_1, k_2, k_3, we can find the 4-th curvature using the equation
k_4 = k_1 + k_2 + k_3 ± 2sqrt(k_1k_2 + k_1k_3 + k_2k_3)

Start with 3 circles of radius 1, then we find curvature of k_4 = 3 ± 2sqrt(3)
3 + 2sqrt(3) is + therefore in is inside the other circles and its radius is +1/(3 + 2sqrt(3))
3 - 2sqrt(3) is - therefore it is circumscribing the other 3 circles and its radius i -1/(3 - 2sqrt(3))

Anwser:
    0.00396087
--- 0.04708099365234375 seconds ---
'''
import time, math
start_time = time.time()

def circle_area(r):
    return math.pi*r*r

def find_curvature(k1, k2, k3):
    c = k1 + k2 + k3
    t = 2*math.sqrt(k1*k2 + k1*k3 + k2*k3)
    return c + t

def find_area_covered(k1, k2, k3, depth): #Recursive method for practice
    
    k4 = find_curvature(k1, k2, k3)
    r = 1/k4
    accumlated_area = circle_area(r)
    if depth == 1:
        return accumlated_area
    
    accumlated_area += find_area_covered(k1, k2, k4, depth - 1)
    accumlated_area += find_area_covered(k2, k3, k4, depth - 1)
    accumlated_area += find_area_covered(k1, k3, k4, depth - 1)  
    
    return accumlated_area
    
def compute(depth_limit): #Recursive method for practice
    #append is an exepsnsive function so I wrote a recursive version as well
    MainCurv = 3 - 2*math.sqrt(3)
    MainRadius = -1/MainCurv
    total_area = circle_area(MainRadius)
    
    total_accumlated_area = 3*circle_area(1)
    total_accumlated_area += 3*find_area_covered(MainCurv, 1, 1, depth_limit)
    total_accumlated_area += find_area_covered(1, 1, 1, depth_limit)

    return round((total_area - total_accumlated_area)/total_area, 8)

def compute_slow(depth_limit):
    MainCurv = 3 - 2*math.sqrt(3) #This is the main circle with radius 3 - 2*math.sqrt(3) from our inital calulcations
    MainRadius = -1/MainCurv
    total_area = circle_area(MainRadius)
    
    total_accumlated_area = 3*circle_area(1) #Start with 3 circles of radius 1
    
    #create 2 stacks to keep track of which new circles we need to find
    #We need 2 for the because we want to calculate the v-piece and center piece seperately
    stack_v_piece = [[MainCurv, 1, 1, depth_limit]] #We start with the big circle and 2 radius 1 circles 
    stack_center_piece = [[1, 1, 1, depth_limit]] #We start with 3 radius 1 circles to find the center circle
    
    while len(stack_v_piece) != 0:
        k1, k2, k3, depth = stack_v_piece.pop(0)
        k4 = find_curvature(k1, k2, k3)
        r = 1/k4
        total_accumlated_area += 3*circle_area(r) #add 3 times the area to account for the 3 v pieces
        if depth > 1:
            stack_v_piece.append([k1, k2, k4, depth - 1])
            stack_v_piece.append([k1, k3, k4, depth - 1])
            stack_v_piece.append([k2, k3, k4, depth - 1])
    
    while len(stack_center_piece) != 0:
        k1, k2, k3, depth = stack_center_piece.pop(0)
        k4 = find_curvature(k1, k2, k3)
        r = 1/k4
        total_accumlated_area += circle_area(r)
        if depth != 1:
            stack_center_piece.append([k1, k2, k4, depth - 1])
            stack_center_piece.append([k1, k3, k4, depth - 1])
            stack_center_piece.append([k2, k3, k4, depth - 1])

    return round((total_area - total_accumlated_area)/total_area, 8)
        
if __name__ == "__main__":
    print(compute(10))
    #print(compute_slow(11))
    print("--- %s seconds ---" % (time.time() - start_time))