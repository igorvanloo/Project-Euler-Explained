#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:34:42 2021

@author: Igor Van Loo
"""
'''
Project Euler Problem 153

Suppose z = a + bi, if z divides d and g = gcd(a, b) then

d/(g(a1 + b1i)) = d(a1 - b1i)/(g(a1*a1 + b1*b1))

Therefore g(a1*a1 + b1*b1) must divide d for z to be a divisor of d

Now we remember the simple case:
    
    1. If b = 0, then we have the basic case of sum of all divisors which is simply sum_{x = 1}^N a * N//a
    
    2. Let's apply the same logic to which numbers a + bi divides, well we know that a + bi = g(a1 + b1i) divides d
    if g(a1*a1 + b1*b1) divides d, so first we simply enumerate all a, b such that 1 = gcd(a, b), then let v = a*a + b*b < N and for each pair we 
    add 2a + 2b, since we get 4 different divisors (a + bi, a - bi, b + ai, b - ai). We store this in a dictionary so that d[v] += 2a + 2b.
    
    Then we can simply go through the dictionary, for each v in d, we can enumerate each multiple of v such that gv <= N and
    do the same sum as in case 1, that is sum_{v in d} d[x] sum_{g = 1}^{N//v} g * N // gx
    
    3. From all this we have missed out the case of z = 1 + i, in this case our set of 4 divisors becomes 2 (1 + i, 1 - i) so it only contributes 2
    so we set d[2] = 2 and apply the same sum as before

Anwser:
    17971254122360635
--- 126.34967136383057 seconds ---
'''

import time, math
start_time = time.time()

def S(N):
    d = {1:1, 2:2}
    for a in range(1, int(math.sqrt(N)) + 1):
        for b in range(a + 1, int(math.sqrt(N - a*a)) + 1):
            if math.gcd(a, b) == 1:
                v = a*a + b*b
                if v in d:
                    d[v] += 2*a + 2*b
                else:
                    d[v] = 2*a + 2*b
    
    total = 0
    for v in d:
        for g in range(1, N//v + 1):
            total += d[v] * g * (N // (g*v))
            
    return total
    
if __name__ == "__main__":
    print(S(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))