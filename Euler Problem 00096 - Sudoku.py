#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:54:09 2021

@author: igorvanloo
"""
'''
Project Euler Problem 96

Sudoku's'

Anwser:
    24702
--- 21.57381510734558 seconds ---    
'''

import time
start_time = time.time()

def ReadFile(): #Create the inital list 
    file = open("/Users/igorvanloo/Dropbox/My Mac (Igors-MacBook-Air.local)/Desktop/Project Euler/0. Files/p096_sudoku.txt")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        datalist.append(x)
    data2list = []
    for z in datalist:
        if "Grid" in z:
            pass
        else:
            temp = [int(y) for y in list(z)]
            data2list.append(temp)
            
    data3list = []
    for i in range(0, len(data2list), 9):
        data3list += [data2list[i:i+9]]
        
    return data3list

listofsudokus = ReadFile()
    
def FindEmptySlot(sudoku): #Finds the empty slots of the sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i,j)
    return None
            
def IsPositionValid(sudoku, position, number): #Position = (i, j) = (row, column)
    
    for i in range(9): #Check if its in the same row
        if sudoku[position[0]][i] == number:
            if i != position[1]:
                return False
    
    for i in range(9): #Check if its in the same column
        if sudoku[i][position[1]] == number:
            if i != position[0]:
                return False 
    
    if position[0] < 3:
        start_x = 0
        end_x = 3
    elif position[0] >= 3 and position[0] < 6:
        start_x = 3
        end_x = 6
    elif position[0] >= 6:
        start_x = 6
        end_x = 9
        
    if position[1] < 3:
        start_y = 0
        end_y = 3
    elif position[1] >= 3 and position[1] < 6:
        start_y = 3
        end_y = 6
    elif position[1] >= 6:
        start_y = 6
        end_y = 9
        
    for i in range(start_x, end_x): #Check box
        for j in range(start_y, end_y):
            if sudoku[i][j] == number:
                if i != position[0] and j != position[1]:
                    return False
    return True
    
def SolveSudoku(sudoku):
    
    emptyslot = FindEmptySlot(sudoku)
    if emptyslot != None:
        row, column = emptyslot
    else:
        
        return True
    
    for i in range(1,10):
        if IsPositionValid(sudoku, (row, column), i):
            sudoku[row][column] = i
            
            if SolveSudoku(sudoku) == True:
                return True
            
            sudoku[row][column] = 0
    
    return False

def compute():
    
    total = 0
    for i in range(0,50):
        SolveSudoku(listofsudokus[i])
        tempsum = int(str(listofsudokus[i][0][0]) + str(listofsudokus[i][0][1]) + str(listofsudokus[i][0][2]))
        total += tempsum    
    return total

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))