# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:28:11 2024

@author: Igor Van Loo
"""
'''
Project Euler Problem 862

Copying from problem 885

There are (n + 9)C9 increasing strings 

Think of stars and bars, imagine you have an n-digit number place the first bar once you've gone
past the 0's, then the 1', etc. There are 9 bars, n digits and you need to choose where to place the nine bars

Example:
    d_0|d_1d_2d_3d_4|||||||| = 01111
    d_0|d_1d_2d_3||||||||d_4 = 01119
    d_0|d_1d_2||d_3||||||d_4 = 01139
    
Then there for n = 12 we have 21C9 = 293,930 possibilities, we can brute force.

Now we need to count the number of substrings exclusing leading 0s. This is because we are not interested
in the actual ordering but rather the size of the set since if we have as shown 9 ways to order (0, 2, 2, 3)
we know that the sum of T(n) for the 9 n is going to be 9*8/2 = 36 since T(2023) = 8, T(2032) = 7, etc

for each possibility x of length n

let d_i = #of digit i in x

Now count number of ways to permute all the digits except 0, this is (d_1 + ... d _9)!/ prod d_i!
Now we place our 0s inbetween them excluding at the front. That is we have n - 1 choice to put our 0s
that is n - 1 C d_0

total is (d_1 + ... d _9)!/ prod d_i! * n - 1 C d_0 = (n - d_0)! * (n - 1)! / (n - 1 - d_0)! / prod d_i!

Answer:
    6111397420935766740
--- 1.4457035064697266 seconds ---
'''

import time, math, itertools
start_time = time.time()

def T(n):
    l = sorted([int("".join(y)) for y in set(itertools.permutations(str(n)))])
    v = len(l) - l.index(n) - 1
    return v
    
def brute_S(n):
    total = 0
    for x in range(10**(n - 1), 10**n):
        total += T(x)
    return total

def S(n):
    total = 0
    for x in itertools.combinations_with_replacement("0123456789", n):
        d = [x.count(str(i)) for i in range(10)]
        t = math.factorial(n - 1) * (n - d[0])
        for v in range(10):
            t //= math.factorial(d[v])
        total += t*(t - 1)//2
    return total
        
if __name__ == "__main__":
    print(S(12))
    print("--- %s seconds ---" % (time.time() - start_time))

