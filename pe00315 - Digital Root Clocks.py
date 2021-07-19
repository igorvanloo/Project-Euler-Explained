#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:02:54 2021

@author: igorvanloo
"""

'''
Project Euler Problem 315

Sam and Max are asked to transform two digital clocks into two "digital root" clocks.
A digital root clock is a digital clock that calculates digital roots step by step.

When a clock is fed a number, it will show it and then it will start the calculation, showing all the intermediate values 
until it gets to the result.
For example, if the clock is fed the number 137, it will show: "137" → "11" → "2" and then it will go black, waiting for 
the next number.

Every digital number consists of some light segments: three horizontal (top, middle, bottom) and four vertical 
(top-left, top-right, bottom-left, bottom-right).
Number "1" is made of vertical top-right and bottom-right, number "4" is made by middle horizontal and vertical 
top-left, top-right and bottom-right. Number "8" lights them all.

The clocks consume energy only when segments are turned on/off.
To turn on a "2" will cost 5 transitions, while a "7" will cost only 4 transitions.

Sam and Max built two different clocks.

Sam's clock is fed e.g. number 137: the clock shows "137", then the panel is turned off, then the next number ("11") 
is turned on, then the panel is turned off again and finally the last number ("2") is turned on and, after some time, off.
For the example, with number 137, Sam's clock requires:

"137"	:	(2 + 5 + 4) × 2 = 22 transitions ("137" on/off).
"11"	:	(2 + 2) × 2 = 8 transitions ("11" on/off).
"2"	:	(5) × 2 = 10 transitions ("2" on/off).
For a grand total of 40 transitions.
Max's clock works differently. Instead of turning off the whole panel, it is smart enough to turn off only those segments 
that won't be needed for the next number.
For number 137, Max's clock requires:

"137"

:

2 + 5 + 4 = 11 transitions ("137" on)
7 transitions (to turn off the segments that are not needed for number "11").
"11"


:


0 transitions (number "11" is already turned on correctly)
3 transitions (to turn off the first "1" and the bottom part of the second "1";
the top part is common with number "2").
"2"

:

4 transitions (to turn on the remaining segments in order to get a "2")
5 transitions (to turn off number "2").
For a grand total of 30 transitions.
Of course, Max's clock consumes less power than Sam's one.
The two clocks are fed all the prime numbers between A = 107 and B = 2×107.
Find the difference between the total number of transitions needed by Sam's clock and that needed by Max's one.

Anwser:
    13625242
--- 24.8354549407959 seconds ---
    
'''

import time, math, eulerlib
start_time = time.time()

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

def LinesNeededSam(number):
    if number == 0:
        return 6
    elif number == 1:
        return 2
    elif number == 2:
        return 5
    elif number == 3:
        return 5
    elif number == 4:
        return 4
    elif number == 5:
        return 5
    elif number == 6:
        return 6
    elif number == 7:
        return 4
    elif number == 8:
        return 7
    elif number == 9:
        return 6
    
def SamClock(startnumber):
    curr = startnumber
    linesum = 0
    while curr >= 10:
        curr = str(curr)
        currlinesum = 0
        for x in curr:
            currlinesum += LinesNeededSam(int(x))
        currlinesum *= 2
        linesum += currlinesum
        curr = sum_digits(int(curr))
    linesum += 2*LinesNeededSam(curr)
    return linesum

def LinesNeededMax(start, end):
    
    start = int(start)
    
    try:
        end = int(end)
    except ValueError:
        pass
    
    #print("test", start, end)
    
    if start == 0:
        if end == 0:
            return 0
        elif end == 1:
            return 4
        elif end == 2:
            return 3
        elif end == 3:
            return 3
        elif end == 4:
            return 4
        elif end == 5:
            return 3
        elif end == 6:
            return 2
        elif end == 7:
            return 2
        elif end == 8:
            return 1
        elif end == 9:
            return 2
        elif end == "o":
            return 6
        
    elif start == 1:
        if end == 0:
            return 4
        elif end == 1:
            return 0
        elif end == 2:
            return 5
        elif end == 3:
            return 3
        elif end == 4:
            return 2
        elif end == 5:
            return 5
        elif end == 6:
            return 6
        elif end == 7:
            return 2
        elif end == 8:
            return 5
        elif end == 9:
            return 4
        elif end == "o":
            return 2 
    
    elif start == 2:
        if end == 0:
            return 3
        elif end == 1:
            return 5
        elif end == 2:
            return 0
        elif end == 3:
            return 2
        elif end == 4:
            return 5
        elif end == 5:
            return 4
        elif end == 6:
            return 3
        elif end == 7:
            return 5
        elif end == 8:
            return 2
        elif end == 9:
            return 3
        elif end == "o":
            return 5
    
    elif start == 3:
        if end == 0:
            return 3
        elif end == 1:
            return 3
        elif end == 2:
            return 2
        elif end == 3:
            return 0
        elif end == 4:
            return 3
        elif end == 5:
            return 2
        elif end == 6:
            return 3
        elif end == 7:
            return 3
        elif end == 8:
            return 2
        elif end == 9:
            return 1
        elif end == "o":
            return 5
        
    elif start == 4:
        if end == 0:
            return 4
        elif end == 1:
            return 2
        elif end == 2:
            return 5
        elif end == 3:
            return 3
        elif end == 4:
            return 0
        elif end == 5:
            return 3
        elif end == 6:
            return 4
        elif end == 7:
            return 2
        elif end == 8:
            return 3
        elif end == 9:
            return 2
        elif end == "o":
            return 4
        
    elif start == 5:
        if end == 0:
            return 3
        elif end == 1:
            return 5
        elif end == 2:
            return 4
        elif end == 3:
            return 2
        elif end == 4:
            return 3
        elif end == 5:
            return 0
        elif end == 6:
            return 1
        elif end == 7:
            return 3
        elif end == 8:
            return 2
        elif end == 9:
            return 1
        elif end == "o":
            return 5
        
    elif start == 6:
        if end == 0:
            return 2
        elif end == 1:
            return 6
        elif end == 2:
            return 3
        elif end == 3:
            return 3
        elif end == 4:
            return 4
        elif end == 5:
            return 1
        elif end == 6:
            return 0
        elif end == 7:
            return 4
        elif end == 8:
            return 1
        elif end == 9:
            return 2
        elif end == "o":
            return 6
        
    elif start == 7:
        if end == 0:
            return 2
        elif end == 1:
            return 2
        elif end == 2:
            return 5
        elif end == 3:
            return 3
        elif end == 4:
            return 2
        elif end == 5:
            return 3
        elif end == 6:
            return 4
        elif end == 7:
            return 0
        elif end == 8:
            return 3
        elif end == 9:
            return 2
        elif end == "o":
            return 4
        
    elif start == 8:
        if end == 0:
            return 1
        elif end == 1:
            return 5
        elif end == 2:
            return 2
        elif end == 3:
            return 2
        elif end == 4:
            return 3
        elif end == 5:
            return 2
        elif end == 6:
            return 1
        elif end == 7:
            return 3
        elif end == 8:
            return 0
        elif end == 9:
            return 1
        elif end == "o":
            return 7
        
    elif start == 9:
        if end == 0:
            return 2
        elif end == 1:
            return 4
        elif end == 2:
            return 3
        elif end == 3:
            return 1
        elif end == 4:
            return 2
        elif end == 5:
            return 1
        elif end == 6:
            return 2
        elif end == 7:
            return 2
        elif end == 8:
            return 1
        elif end == 9:
            return 0
        elif end == "o":
            return 6


def MaxClock(startnumber):
    curr = str(startnumber)
    linesum = 0
    
    for x in curr:
        linesum += LinesNeededSam(int(x))
    
    #print(linesum)
            
    while True:
        curr = str(curr)
        nextnum = str(sum_digits(int(curr)))

        
        value = len(curr) - len(nextnum)
        temp = value*'o' + (nextnum)
        #print(curr, temp)
        
        for y in range(len(curr)):
            #print((curr[y]), (temp[y]))
            linesum += LinesNeededMax((curr[y]), (temp[y]))
            #print(linesum)
            
        curr = nextnum
        
        if int(curr) < 10:
            linesum += LinesNeededSam(int(curr))
            break
    return linesum
    
def compute(start, end):
    finalprimes = [x for x in eulerlib.primes(end) if x > start]
    
    print("done with primes")
    total = 0
    for y in finalprimes:
        total += SamClock(y) - MaxClock(y)
        
    return total
        
if __name__ == "__main__":
    #print(compute(59800, 100000))
    print(compute(1000, 100000))
    print("--- %s seconds ---" % (time.time() - start_time))