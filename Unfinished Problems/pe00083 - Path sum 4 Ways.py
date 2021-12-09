#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 21:00:50 2021

@author: igorvanloo
"""

'''
Project Euler Problem 83

Tried something with bellmandford algorithm but not working 

Anwser:

'''

import time

def ReadFile(): #Create the inital list 
    file = open("/Users/igorvanloo/Dropbox/My Mac (Igors-MacBook-Air.local)/Desktop/Python Projects/0. Files/p082_matrix.txt")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        datalist.append(x)
        
    data2list = []
    for x in datalist:
        temp = x.split(',')
        temp = [int(i) for i in temp]
        data2list.append(temp)
    return data2list

def compute():
    #matrix = ReadFile()

    matrix = [[131, 673, 234, 103,18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]    
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    INF = 10**10
    
    mask = [[INF]*columns for i in range(rows)]
    marked = [[0]*columns for i in range(rows)]
    
    mask[0][0] = matrix[0][0]
    marked[0][0] = 1
    
    def distance_to(x,y):
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return INF
        else:
            if marked[x][y] == 1:
                return INF
            else:
                return matrix[x][y]
    
    currx, curry = (0,0)
    path = [matrix[0][0]]
    while True:
        
        up = [distance_to(currx-1, curry), (currx-1, curry)]
        down = [distance_to(currx+1, curry), (currx+1, curry)]
        right = [distance_to(currx, curry + 1), (currx, curry + 1)]
        left = [distance_to(currx, curry-1), (currx, curry-1)]
        
        for x in [up, down, right, left]:
            if x[0] != INF:
                i, j = x[1]
                mask[i][j] = (x[0])
                #print(mask)
                #print([up, down, right, left])
        
        minimum = min(up, down, right, left)
        
        if currx == rows-1 and curry == columns-1:
            break
        path.append(minimum[0])
        currx, curry = minimum[1]
        marked[currx][curry] = 1
    return sum(path)

def bellmanford():
    #matrix = ReadFile()

    matrix = [[131, 673, 234, 103,18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]    
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    INF = 10**10
    
    mask = [[INF]*columns for i in range(rows)]
    
    mask[0][0] = matrix[0][0]
    
    def distance_to(x,y):
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return INF
        else:
            return mask[x][y]
    
    change = True
    while change:
        change = False
        for x in range(rows):
            for y in range(columns):
                temp = (matrix[x][y] + min(distance_to(x-1, y), distance_to(x+1, y), distance_to(x, y-1), distance_to(x, y+1)))
                if temp < mask[x][y]:
                    mask[x][y] = temp
                    change = True
        
    return mask
    
if __name__ == "__main__":
    start_time = time.time()
    print(bellmanford())
    print("--- %s seconds ---" % (time.time() - start_time))