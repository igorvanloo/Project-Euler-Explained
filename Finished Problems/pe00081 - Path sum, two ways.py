#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:46:33 2021

@author: igorvanloo
"""
'''
Project Euler Problem 81

Anwser:
    427337
--- 0.004037141799926758 seconds ---
'''

import time
start_time = time.time()

def ReadFile(): #Create the inital list 
    file = open("/Users/igorvanloo/Dropbox/My Mac (Igors-MacBook-Air.local)/Desktop/Python-Projects/Project-Euler-Related/0. Project Euler Files/p082_matrix.txt")
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
    '''matrix = [[131, 673, 234, 103,18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]'''
    
    y = len(matrix)
    x = len(matrix[0])
    for i in (range(x)):
        for j in (range(y)):
            if i - 1 >= 0 and j - 1 >= 0:
                temp = min(matrix[i-1][j], matrix[i][j-1])
            elif i - 1 >= 0:
                temp = matrix[i-1][j]
            elif j - 1 >= 0:
                temp = matrix[i][j-1]
            else:
                temp = 0
            matrix[i][j] += temp
    return matrix

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))