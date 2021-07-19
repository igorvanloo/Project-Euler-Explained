#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:31:40 2020

@author: igorvanloo
"""

'''
Project Euler Problem 

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual 
in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations 
of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

Anwser:
    
    296962999629
--- 0.051260948181152344 seconds ---
'''

import time, math, eulerlib, itertools
start_time = time.time()

def compute():
    primes_to_check = sorted(list(set(eulerlib.primes(10000)) - set((eulerlib.primes(1000)))))
    
    for x in range(len(primes_to_check)):
        temp_permutation = sorted(list(set(itertools.permutations(str(primes_to_check[x]))))) #sorted to ensure ascending order
        count = 0
        possible_seq = []
        for y in range(len(temp_permutation)):
            
            temp_var = "".join(str(temp_permutation[y][i]) for i in range(4))
              
            if int(temp_var) in primes_to_check:
                
                count += 1
                possible_seq.append(int(temp_var))

                if count >= 3:
                    for i in range(len(possible_seq)):
                        for j in range(i,len(possible_seq)):
                            for k in range(i,len(possible_seq)):
                                if possible_seq[j] - possible_seq[i] == possible_seq[k] - possible_seq[j] and possible_seq[j] - possible_seq[i] != 0:
                                    anwser_str = str(possible_seq[i]) + str(possible_seq[j]) + str(possible_seq[k])
                                    if anwser_str != "148748178147":
                                        return anwser_str
                                
                            

                    
                    

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))