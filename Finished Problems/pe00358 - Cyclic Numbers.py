#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:26:46 2022

@author: igorvanloo
"""
'''
Project Euler Problem 358

https://en.wikipedia.org/wiki/Cyclic_number

Primes generate this cycles, has to be between 724600000 and 730000000 through some trial and error
I use fermats little theorem to quickly guess if a number is a prime and then check ifs its last 5 digits are 56789
I get 3 guesses 725509891, 726509891, 729809891 and the question states this must be unique therefore it must have a cycle of length p-1

Then using sum_decimals I find that 
725509891 has a period length of 145101978 which is not 725509890 so this is not the prime which generates the cycle
726509891 has a period length of 145301978 which is not 726509890 so this is not the prime which generates the cycle
729809891 has a period length of 145101978 which is 729809890 so this is the prime which generates the cycle

the sum of its digits is 3284144505

Anwser:
    3284144505
    Didn't actually run the function just did it in steps
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
    
def sum_decimals(num, den):
    num_digits = 0
    digit_sum = 0
    while True:
        num *= 10
        temp = math.floor(num/den)
        digit_sum += temp
        num_digits += 1
        num -= temp*den
        if num == 1:
            break
    return digit_sum, num_digits
    
def compute():
    start = int((10**11/138))
    end = int((10**11/137))
    for x in range(start, end):
        if pow(2, x, x) == 2 and pow(3, x, x) == 3: #Fermats little theorem
            if is_prime(x):
                if (56789 * x) % 100000 == 99999 and (((56789 * x) + 1) % 100000) == 0:
                    digit_sum, num_digits = sum_decimals(1, x)
                    if num_digits == (x-1):
                        return digit_sum
    
if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))

