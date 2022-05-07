#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 21:00:50 2021

@author: igorvanloo
"""

'''
Project Euler Problem 83

Used DijkstrasAlgorithm

Anwser:
    425185
--- 1.0952627658843994 seconds ---
'''
import time

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

def DijkstrasAlgorithm():
    
    matrix = ReadFile()

    '''matrix = [[131, 673, 234, 103,18],
             [201, 96, 342, 965, 150],
             [630, 803, 746, 422, 111],
             [537, 699, 497, 121, 956],
             [805, 732, 524, 37, 331]]'''
    
    rows = len(matrix)
    columns = len(matrix[0])
    INF = 10**8
    
    unvisisted_nodes = dict()
    for x in range(rows):
        for y in range(columns):
            unvisisted_nodes[(x, y)] = INF
    unvisisted_nodes[(0, 0)] = matrix[0][0]
    
    mask = [[INF]*columns for i in range(rows)]
    mask[0][0] = matrix[0][0]
        
    def visit_neighbour(og_x, og_y, x, y, unvisisted_nodes):
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return False
        if (x, y) in unvisisted_nodes:
            return min(mask[x][y], mask[og_x][og_y] + matrix[x][y])
    
    curr = (0, 0)
    while True:
        x, y = curr
        for (a, b) in ((x + 1, y), (x, y+ 1), (x - 1, y), (x, y - 1)):
            temp = visit_neighbour(x, y, a, b, unvisisted_nodes)
            if temp:
                mask[a][b] = temp
                unvisisted_nodes[(a, b)] = temp
    
        unvisisted_nodes.pop(curr)
        if len(unvisisted_nodes) != 0:
            curr = min(unvisisted_nodes, key=unvisisted_nodes.get)
        else:
            break
    
    return mask[rows - 1][columns - 1]
    
if __name__ == "__main__":
    start_time = time.time()
    print(DijkstrasAlgorithm())
    print("--- %s seconds ---" % (time.time() - start_time))