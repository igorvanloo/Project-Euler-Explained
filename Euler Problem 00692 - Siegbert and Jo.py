#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:18:12 2021

@author: igorvanloo
"""

'''
Project Euler Problem 692

Siegbert and Jo take turns playing a game with a heap of N pebbles:
1. Siegbert is the first to take some pebbles. He can take as many pebbles as he wants. (Between 1 and N inclusive.)
2. In each of the following turns the current player must take at least one pebble and at most twice the amount of pebbles 
taken by the previous player.
3. The player who takes the last pebble wins.

Although Siegbert can always win by taking all the pebbles on his first turn, to make the game more interesting he 
chooses to take the smallest number of pebbles that guarantees he will still win 
(assuming both Siegbert and Jo play optimally for the rest of the game).

H(N) = minimum 

G(n) = sum of H(N) from 1 to n

find G(23416728348467685)

Fibonnaci Nim is what the game is called,

It is easily solved by taken the lowest number in the zeckendorf representation of a number, and if the number is a fibonnaci
then player 1 must take the entire pile to win

Obviously adding up one by one will take forever as the number is too large, so we must think of a smarter way
Producing the first few numbers and taking their minimum, we beging to see a pattern, that is linked to fibonnaci numbers

Notice that 23416728348467685 is for some reason a fibonnaci

Take N = f(n) to be a fibonnaci number

We notice that G(f(n)) = G(f(n-1)) + G(f(n-2)) - f(n-2) + f(n) for fibonnnaci numbers

Example
G(21) = 79
G(13) = 43
G(8) = 23
f(n-2) = 8
f(n) = 21
43 + 23 - 8 + 21 = 79


We we simple iterate from the fibonnaci 23416728348467685

Anwser:
    842043391019219959
--- 0.016277074813842773 seconds ---
    
'''

import time
start_time = time.time()

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2

def Fibtill(x):
    fibnumbers = []
    n = 1
    while len(fibnumbers) != x:
        fibnumbers.append(fibonnaci(n))
        n += 1
    return fibnumbers

def ZeckendorfRepresentation(x, fibnumbers):
    rep = []
    number = x
    count = 0
    while number != 0:
        
        if number - fibnumbers[count] >= 0:
            number -= fibnumbers[count]
            rep.append(fibnumbers[count])
            count += 1
        count += 1
        
    return rep

#fibnumbers = Fibtill(23416728348467685)
    
def G1(x):
    g1 = 1
    g2 = 1
    
    f1 = 1
    f2 = 1
    
    count = 2
    while count != x:
        fn = f1 + f2
        #print(fn)
        
        gn = g1 + g2 - f1 + fn
        #print("1", gn)

        f1 = f2
        f2 = fn
        
        g1 = g2
        g2 = gn
        
        count += 1
    return gn


if __name__ == "__main__":
    print(G1(70))
    print("--- %s seconds ---" % (time.time() - start_time))