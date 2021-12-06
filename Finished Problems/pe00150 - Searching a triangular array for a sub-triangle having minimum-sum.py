#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:16:54 2021

@author: igorvanloo
"""

'''
Project Euler Problem 150

Generate the triangle in a triangle format so it's easier to understand what you are doing

If you start at an apex (a,b) then you can form triangles 

Anwser:
    -271248680
--- 43.593997955322266 seconds ---
'''

import time
start_time = time.time()

def s_generator():
    t = 0
    s = []
    for k in range(1,500501):
        t = (615949*t + 797807) % 2**20
        s.append(t - 2**19)
    
    triangle = []
    
    r = 1000
    while r != 0:
        row = []
        for x in range(r):
            temp = s.pop(-1)
            row.insert(0,temp)
        triangle.insert(0, row)
        r -= 1

    return triangle


def compute():
    triangle = s_generator()
    
    row_sum_triangle = s_generator()
    
    for row in range(len(row_sum_triangle)):
        row_sum_triangle[row].insert(0,0)
        for col in range(1, len(row_sum_triangle[row])):
            row_sum_triangle[row][col] += row_sum_triangle[row][col-1]
    #With this we have a running total of the sum in a row, so if we want to calculate a partial sum say from
    #triangle[5][2] to triangle[5][6] all we need is row_sum_triangle[5][6] - row_sum_triangle[5][1]
    minimum = 0
    for x in range(len(triangle)): #Denotes row
        for y in range(len(triangle[x])): #Denotes position in row
        
            curr_sum = triangle[x][y]
            if curr_sum < minimum:
                minimum = curr_sum
                
            curr_y = y + 2 #We need to offset by 2 because row_sum_triangle 
            for next_x in range(x+1,1000):
                curr_sum += row_sum_triangle[next_x][curr_y] - row_sum_triangle[next_x][y]
                if curr_sum < minimum:
                    minimum = curr_sum
                curr_y += 1
            
    return minimum

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))