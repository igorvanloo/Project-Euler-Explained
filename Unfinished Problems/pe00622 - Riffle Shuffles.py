# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:06:37 2022

@author: IP176077
"""
'''
Project Euler Problem 622

For some reason the "Riffle suffle" is actually known as the Faro Shuffle: https://en.wikipedia.org/wiki/Faro_shuffle
Specifically we are talking about a faro out-shuffle

In general, k perfect in-shuffles will restore the order of an n-card deck if 2^{k} = 1 (mod n - 1)
For example, 8 consecutive iout-shuffles restore the order of a 52-card deck, because 2^{8} = 256 = 1 (mod 51)

Therefore, the sum of all n s.t. s(n) = 8 is all n s.t. 2^8 = 1 (mod n - 1) 
and no divisor of n does it as well

2^8 - 1 = (n - 1)l => 255 = (n - 1)l

Therefore we find the divisors of 255, they are our candidate numbers.
For each candidate number, x, we check if 2^n (mod x) = 1, if yes then we need to check it is indeed the smallest
Knowing that 2^n = 1 (mod x), we know that either this is the order of 2 or a divisor of 60 is,
simply check each divisor of 60

Anwser:
    3010983666182123972
--- 96.2194402217865 seconds ---
'''
import time, math
start_time = time.time()
        
def Divisors_of(x):  # Find the divisors of a number
    divisors = set([x])
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(x//i)
    return list(sorted(divisors))

def compute(n):
    div = Divisors_of(pow(2, n) - 1)
    div_n = Divisors_of(n)
    total = 0
    # We go through the divisors of 2^n - 1 = xk
    for x in div:
        # We test to see if 2^n = 1 (mod x)
        if pow(2, n, x) == 1:
            # Now we know 2^n = 1 (mod x), now we test if any divisor, y, of n does it earlier
            # Because then s(x + 1) = y
            if all([pow(2, y, x) != 1 for y in div_n[:len(div_n) - 1]]):
                total += (x + 1) 
    return total

if __name__ == "__main__":
    print(compute(60))
    print("--- %s seconds ---" % (time.time() - start_time))