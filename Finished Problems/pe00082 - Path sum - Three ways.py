#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 23:01:40 2021

@author: igorvanloo
"""
'''
Project Euler Problem 82

Anwser:
    260324
--- 0.1475849151611328 seconds ---
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
    matrix = ReadFile()
    
    """matrix = [[131, 673, 234, 103,18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]"""
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    mask = [[0]*columns for i in range(rows)]
    
    for x in range(rows):
        mask[x][0] = matrix[x][0]
        
    def mindistance(x,y): 
        #This function will find the minimum distance from every cell in the previous column
        #to the currect cell (x,y)
        lengths = []
        up_curr = 0 #This will keep a running total of the matrix cells above the starting cell
        for up in range(x-1, -1, -1):
            #This will append the length of the cells up and to the left
            lengths.append(up_curr + matrix[up][y] + mask[up][y-1])
            up_curr += matrix[up][y] #Updated the down_curr
        
        down_curr = 0 #Same as above
        for down in range(x+1, rows):
            lengths.append(down_curr + matrix[down][y] + mask[down][y-1])
            down_curr += matrix[down][y]
        return min(lengths) #We return the least value (shortest path)
            
    for y in range(1,columns):
        for x in range(rows):
            mask[x][y] += (matrix[x][y] + min(mask[x][y-1], mindistance(x,y)))
            
    return min([mask[x][columns-1] for x in range(0, rows)])
if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))