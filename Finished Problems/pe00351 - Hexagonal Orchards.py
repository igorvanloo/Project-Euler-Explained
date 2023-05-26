# -*- coding: utf-8 -*-
"""
Created on Fri May 26 13:16:34 2023

@author: igorvanloo
"""
'''
Project Euler Problem 351

Clearly we only need to look at one section (triangle) of the hexagon and then we multiply by 6

Now from the center of the hexagon we draw a line to each of the next 2 points

Lets say the the center to the point to the right (if we look at the top right triangle) this is clearly
at an angle of 0, then from the center to the next of the 2 points lets denote this as angle 1

Now we draw to the next 3 points
The first point clearly still has angle 0, last point has angle 1 hence they are in the shadow
What about the second point? well it is clearly right in the center of first and third point, hence
it has angle 1/2

The pattern is clear:
    first layer has angles 0/1, 1/1
    second layer has angles 0/2, 1/2, 2/2
    third layer has angles 0/3, 1/3, 2/3, 3/3
    fourth layer has angles 0/4, 1/4, 2/4, 3/4, 4/4 
    etc

we can see the fourth layer has 2/4 = 1/2 hence it is in the shadow of 1/2

Hence the problem is reduced to the following:
    given an order n hexagonal orchard, we must find the numbers of fractions that are not in reduced form
    that is find all x/n such that gcd(x, n) > 1
    
    excluding the 0/n case, on layer n there are n fractions, finding all 1 <= 1 <= n such that gcd(x, n) > 1
    is the same as n - sum_{x, gcd(x, n) = 1} 1 = n - φ(n)
    
    Therefore for an order n hexagonal orchard we have
    answer = 6 * sum_{i = 1}^n (i - φ(i))
           = 6 * (sum_{i = 1}^n i - sum_{i = 1}^n φ(i))
           = 3*n(n+1) - 6*sum_{i = 1}^n φ(i)
           
https://en.wikipedia.org/wiki/Totient_summatory_function = sum_{i = 1}^n φ(i) 

Anwser:
    11762187201804552
--- 85.1692283153534 seconds ---

After optimization
    11762187201804552
--- 0.9705486297607422 seconds ---
'''
import time, math
start_time = time.time()
    
def mobius_k_sieve(n, k = 2):
    '''
    I redefined the the Mobius function:
                    1 if n is k-free positive integer with even number of prime factors
        μ_{k}(n) = -1 if n is k-free positive integer with odd number of prime factors
                    0 if n has a k power factor
    '''
    prime = [1]*(n + 1)
    prime[0] = prime[1] = 0
    mob = [0] + [1]*(n)
    for p in range(2, n + 1):
        if prime[p]:
            mob[p] *= -1
            for i in range(2*p, n + 1, p):
                prime[i] = 0
                mob[i] *= -1
            sq = pow(p, k)
            if sq <= n:
                for j in range(sq, n + 1, sq):
                    mob[j] = 0
    return mob

def totient_sum_slow(n):
    mob = mobius_k_sieve(n)
    tot = 0
    for k in range(1, n + 1):
        t = n//k
        tot += mob[k]*t*(t + 1)
    return tot//2

def totient_sum(n):
    L = int(math.sqrt(n))
    v = [0]*(L + 1)
    bigV = [0]*(n//L + 1)
    
    for x in range(1, L + 1):
        res = (x*(x + 1))//2
        for g in range(2, int(math.sqrt(x)) + 1):
            res -= v[x//g]
        
        for z in range(1, int(math.sqrt(x)) + 1):
            if x//z != z:
                res -= (x//z - x//(z + 1))*v[z]
        
        v[x] = res
    
    for x in range(n//L, 0, -1):
        k = n//x
        res = (k*(k + 1))//2
        
        for g in range(2, int(math.sqrt(k)) + 1):
            if k//g <= L:
                res -= v[k//g]
            else:
                res -= bigV[x*g]
        
        for z in range(1, int(math.sqrt(k)) + 1):
            if z != k//z:
                res -= (k//z - k//(z + 1))*v[z]
        bigV[x] = res
        
    return bigV[1]

def H(n):
    return 3*n*(n + 1) - 6*totient_sum(n)

if __name__ == "__main__":
    print(H(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))
