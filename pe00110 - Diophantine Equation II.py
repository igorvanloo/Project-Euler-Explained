#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:23:27 2021

@author: igorvanloo
"""

'''
Project Euler Problem 110

From problem 108, we are reducing to finding the minimum n such that n^2 has 4 million factors

if n = p1^a * p2^b * p3^c * ...
then d(n) = (a+1)(b+1)(c+1)... d(n) is the number of divisors

=> d(n^2) = (2a+1)(2b+1)(2c+1)

we need d(n^2) > 8,000,000

Our upper bound is therefore d(n) = 3^15 = 14348907 with n = 2*3*5*7*11*13*17*19*23*29*31*37*41*43*47 = 614889782588491410

List the primes = [2,  3, 5, 7,11,13,17,19,23,29 ,31 ,37 ,41 ,43 ,47 ]
and exponents =   [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15]

Clearly e1 >= e2 >= e3 >= ... >= e14 >= 0 because if not we could just swap them, from example: let n 2^2 * 3^3 => n^2 has 5*7 divisors but n=2^3 * 3^2 also has 5*7 divisors
 
Then given a list of exponents where n = 2^e1 * ... * 43^e14, d(n^2) = (2e1 + 1)*...(2e14 + 1) 
We are looking for (2e1 + 1)*...(2e14 + 1) > 8,000,000

log(614889782588491410, 2) ~ 59, this tells us that we can have a maximum of 60 in the exponent but 2^60 only gives 121 divisors not enough
log(614889782588491410, 6) ~ 22, and so on


Answer:
    9350130049860600
--- 83.21368288993835 seconds ---
'''

import time

def compute(): #Ugliest code known to man
    
    minimum = 614889782588491410
    for e1 in range(1,60):
        print("e1", e1)
        divisors = (2*e1 + 1)
        number = 2**e1

        for e2 in range(1, 23):
            divisors = (2*e1 + 1)*(2*e2 + 1)
            number = 2**e1 * 3**e2
            if number > minimum:
                break
            
            for e3 in range(1,12):
                divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)
                number = 2**e1 * 3**e2 * 5**e3
                if number > minimum:
                    break
                for e4 in range(1,8):
                    divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)
                    number = 2**e1 * 3**e2 * 5**e3 * 7**e4
                    if number > minimum:
                        break
                    for e5 in range(1,6):
                        divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)
                        number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5
                        if number > minimum:
                            break
                        for e6 in range(4):
                            divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)
                            number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6
                            if number > minimum:
                                break
                            for e7 in range(4):
                                divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)
                                number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7
                                if number > minimum:
                                    break
                                for e8 in range(3):
                                    divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)
                                    number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8
                                    if number > minimum:
                                        break
                                    for e9 in range(3):
                                        divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)
                                        number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9
                                        if number > minimum:
                                            break
                                        for e10 in range(2):
                                            divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)      
                                            number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10
                                            if number > minimum:
                                                break
                                            for e11 in range(2):
                                                divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)      
                                                number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11
                                                if number > minimum:
                                                    break
                                                for e12 in range(2):
                                                    divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)*(2*e12 + 1)     
                                                    number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12
                                                    if number > minimum:
                                                        break
                                                    for e13 in range(2):
                                                        divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)*(2*e12 + 1)*(2*e13 + 1)   
                                                        number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12 * 41**e13
                                                        if number > minimum:
                                                            break
                                                        for e14 in range(2):
                                                            divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)*(2*e12 + 1)*(2*e13 + 1)*(2*e14 + 1)   
                                                            number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12 * 41**e13 * 43**e14
                                                            if divisors > 8*10**6 and number < minimum:
                                                                minimum = number
    return minimum

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))