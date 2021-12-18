#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:22:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 329

Wanted Sequence: PPPPNNPPPNPPNPN

Example case Frog starts at x = 15
                                                                                      x = 15 (P, 1 * 1/3)                                     
                                                                x = 14 (P, 1/2 * 1/3),                    x = 16 (P, 1/2 * 1/3)
                                           x = 13 (P, 1/4 * 2/3),                    x = 15 (P, 2/4 * 1/3),                    x = 17 (P, 1/4 * 2/3)
                     x = 12 (P, 1/8 * 1/3),                    x = 14 (P, 3/8 * 1/3),                     x = 16 (P, 3/8 * 1/3),                    x = 18 (P, 1/8 * 1/3)
x = 11 (N, 1/16 * 1/3),                   x = 13 (N, 4/16 * 1/3),                   x = 15 (N, 6/16 * 2/3),                    x = 17 (N, 4/16 * 1/3),                  x = 19 (N, 1/16 * 1/3)


I literally have no idea what i'm doing wrong using Stephane Brummes Website I get the case 
500 1 : correct 
500 2 : correct
500 3 : 6 cases different
500 4 : 450 cases different   
500 5 : 960 cases different  
500 6 : 2100432 cases different
500 7 : 259375104 cases different

Anwser:
    
'''

import time, math
start_time = time.time()

def is_prime(x): #Test if giving value is a prime 
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True
    
def prob(x, letter):
    if is_prime(x):
        if letter == "P":
            return 2
        else:
            return 1
    else:
        if letter == "P":
            return 1
        else:
            return 2

def compute(pathlength, croaks):
    
    seq = "PPPPNNPPPNPPNPN"
    main_num = 0
    main_den = 0
    
    for x in range(1, pathlength + 1):
        
        curr = [x]
        temp_num = prob(x, seq[0])
        temp_den = 3
        
        for y in range(1,croaks):
            temp2_num = 0
            temp2_den = 3 * 2**y
            
            temp = []
            letter = seq[y]
            for z in curr:
                a = z + 1
                b = z - 1
                
                if b == 0:
                    temp.append(a)
                    temp.append(a)
                elif a == (pathlength + 1):
                    temp.append(b)
                    temp.append(b)
                else:
                    temp.append(a)
                    temp.append(b)
            #print(temp)
            curr = temp
            for c in set(curr):
                d = prob(c, letter)
                temp2_num += (temp.count(c) * d)
            temp_num *= temp2_num
            temp_den *= temp2_den
        
        #print(temp_num, temp_den)
        main_num += temp_num
        main_den += temp_den
    print(main_num, main_den)
    g = math.gcd(main_num, main_den)
    return main_num//g, main_den//g

if __name__ == "__main__":
    print(compute(500,7))
    print("--- %s seconds ---" % (time.time() - start_time))