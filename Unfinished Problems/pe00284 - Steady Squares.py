#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 21:46:04 2022

@author: igorvanloo
"""
'''
Project Euler Problem 284

    32c68ca - n = 2000
--- 181.84151124954224 seconds ---
Anwser:

'''
import time, math
start_time = time.time()

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def NumberToBase14(n):
    digits = numberToBase(n, 14)
    new_digits = []
    for x in digits:
        if x == 10:
            new_digits.append("a")
        elif x == 11:
            new_digits.append("b")
        elif x == 12:
            new_digits.append("c")
        elif x == 13:
            new_digits.append("d")
        else:
            new_digits.append(str(x))
    return "".join(new_digits)

def sumdigits(x):
    total = 0
    for y in list(x):
        if y == "a":
            total += 10
        elif y == "b":
            total += 11
        elif y == "c":
            total += 12
        elif y == "d":
            total += 13
        else:
            total += int(y)
    return total
    
def compute(limit):
    
    allnumbers = ["0", "1", "7", "8"]  
    base = ["7", "8"]
    
    for n in range(2, limit + 1):
        print(n)
        temp = []
        for x in base:
            for y in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d"]:
                curr = y + x
                if NumberToBase14(pow(int(curr, 14), 2))[-n:] == curr:
                    temp.append(curr)
                    if y != "0":
                        allnumbers.append(curr) 
                    break
            base = temp
    return NumberToBase14(sum([sumdigits(x) for x in allnumbers]))

if __name__ == "__main__":
    print(compute(2000))
    print("--- %s seconds ---" % (time.time() - start_time))