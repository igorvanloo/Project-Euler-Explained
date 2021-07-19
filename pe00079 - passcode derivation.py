#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:27:10 2020

@author: igorvanloo
"""
'''
Project Euler Problem 79

A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply 
would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest 
possible secret passcode of unknown length.

Im going to find all the numbers first then make a string that will be able to find all of the keycodes

{'0', '9', '8', '6', '2', '3', '1', '7'} These are all the numbers
We guess that the minimum length is 8 as this is the smallest possible

Then I create all possible combinations and check that if all the strings are in this combination then we are done

Anwser:
    73162890
--- 1.2007651329040527 seconds ---
    
'''
import time, math, eulerlib, itertools
start_time = time.time()

SUBSEQS = ["319", "680", "180", "690", "129", "620", "762", "689", "762", "318", "368", "710", "720", "710", "629", "168", "160", "689", "716", "731", "736", "729", "316", "729", "729", "710", "769", "290", "719", "680", "318", "389", "162", "289", "162", "718", "729", "319", "790", "680", "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"]

def all_numers(x):
    temp_var = "".join(str(x[i]) for i in range(len(x)))
    return set(temp_var)

def compute():
    possible_numers = list(all_numers(SUBSEQS))
    possible_passcode = list(itertools.permutations(possible_numers))
    for y in range(len(possible_passcode)):
        count = 0
        for x in range(len(SUBSEQS)):
            a, b, c = SUBSEQS[x][0], SUBSEQS[x][1], SUBSEQS[x][2]
            a_index = possible_passcode[y].index(a)
            b_index = possible_passcode[y].index(b)
            c_index = possible_passcode[y].index(c)
            if a_index < b_index and b_index < c_index:
                count += 1
                if count == 50:
                    temp_var = "".join(str(possible_passcode[y][i]) for i in range(len(possible_passcode[y])))
                    return temp_var
            

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
