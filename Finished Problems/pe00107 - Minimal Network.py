#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:53:55 2021

@author: igorvanloo
"""

'''
Project Euler Problem 107

This is called finding the MST of a graph, I will be using Prim's algorithm 

Anwser:
    259679
--- 0.003554821014404297 seconds ---
'''

import time

def ReadFile(): #Create the graph
    file = open("/Users/igorvanloo/Dropbox/My Mac (Igors-MacBook-Air.local)/Desktop/Python Projects/0. Files/p107_network.txt")
    datalist = []
    for x in file:
        datalist.append(x.split(","))

    final = []
    for x in datalist:
        row = []
        for y in x:
            try:
                row.append(int(y))
            except ValueError:
                if y == "-":
                    row.append(int(0))
        
        if len(row) == 39:
            row.append(0)
            
        final.append(row)
    return final

def PrimsAlgorithm(graph):
    dimension = len(graph)
    Previous_Weight = sum([graph[x][y] for x in range(dimension) for y in range(x+1, dimension) if graph[x][y] != 0])
    
    Tree = set([0])
    
    New_Weight = 0
    
    #We go through the tree and we add the least weighted edge that is connected to one of the vertex's we've already visisted
    
    for x in range(dimension - 1):
        Minimum_edge, Corresponding_vertex = min([(graph[x][y], y) for x in Tree \
                                                  for y in range(dimension) if y not in Tree and graph[x][y] != 0])
        Tree.add(Corresponding_vertex)
        New_Weight += Minimum_edge
        
        if len(Tree) == dimension:
            break
    
    return Previous_Weight - New_Weight

if __name__ == "__main__":
    start_time = time.time()
    print(PrimsAlgorithm(ReadFile()))
    print("--- %s seconds ---" % (time.time() - start_time))