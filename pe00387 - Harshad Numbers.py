#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:35:30 2021

@author: igorvanloo
"""

'''
Project Euler Problem 387

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a 
right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.

Thoughts

Generating primes will take far too long, I will start with the base 1 digit integers and I will build up all the
right trunctable harshad numbers < 10**digit

Once I have these, I will check which of these in the list produce a prime when x / sum_digits(x)

Then I will once again take this final list and add digits 1,3,5,7,9 to the end and check if they are prime,
if they are then they qualify as primes such that removing one digit results in a right trunctable harshad prime, that
when divided by the sum of their digits are prime

Anwser:
    696067597313468
--- 6.786883115768433 seconds ---
    
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
    
def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

def RightTruncHarshadGen(digits):
    base = [str(x) for x in range(0,10)]
    check = [1,2,3,4,5,6,7,8,9]
    righttrunc = [1,2,3,4,5,6,7,8,9]
    while True:
        if len(check) == 0:
            break
        temp = check.pop(0)
        for i in range(0,10):
            curr = int(str(temp) + base[i])            
            if curr % sum_digits(curr) == 0:
                if len(str(curr)) < digits:
                    check.append(curr)
                righttrunc.append(int(curr))
    return righttrunc
    
def compute(limit):
    Harshad = RightTruncHarshadGen(limit)
    candidate = []
    total = 0
    for x in Harshad:
        if is_prime(x / sum_digits(x)) == True:
            candidate.append(x)
    
    check = [1,3,5,7,9]
    for y in candidate:
        for z in check:
            temp = int(str(y) + str(z))
            if is_prime(temp) == True:
                total += temp
    return total

if __name__ == "__main__":
    print(compute(3))
    print("--- %s seconds ---" % (time.time() - start_time))