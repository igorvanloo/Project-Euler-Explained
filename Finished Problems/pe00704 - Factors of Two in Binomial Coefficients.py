# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:16:36 2023

@author: igorvanloo
"""
'''
Project Euler Problem 704

g(n, m) = largest power of 2 dividing nCm
F(n) = max{g(n, m) | 0 <= m <= n}
S(N) = sum_{n = 1}^N F(n)

I remembered legendres formula, which lead me to kummers theorem
https://en.wikipedia.org/wiki/Kummer%27s_theorem

the case p = 2 is especially easy

Write n, m, n-m in base 2 let S(n) = sum of digits of n in base 2
Then highest power of 2 in nCm = S(m) + S(n - m) - S(n)

Since the goal is 10^16 we probably need a O(sqrt(n)) or O(log(n)) algorithm to solve this problem
g(n, m) is O(log(n))

F(n) = https://oeis.org/A119387
Comment shows F(n) = floor(log(n+1)/log(2)) - valuation(n+1,2)

floor(log(n+1)/log(2)) = https://oeis.org/A000523
valuation(n+1,2) = https://oeis.org/A007814 = val(n)

Now S(N) = sum_{n = 1}^N F(n)
         = sum_{n = 1}^N floor(log(n+1)/log(2)) - val(n+1,2)
         = sum_{n = 1}^N floor(log(n+1)/log(2)) - sum_{n = 1}^N val(n+1,2)
         
Looking further into the oeis pages there is a partial sum cf

sum_{n = 1}^N floor(log(n)/log(2)) = https://oeis.org/A061168 = (n+1)*floor(log_2(n)) - 2*(2^floor(log_2(n)) - 1)

sum_{n = 1}^N val(n,2) = n - bit count of n 

In our case we have:
    
    sum_{n = 1}^N floor(log(n + 1)/log(2)) = sum_{n = 1}^(N + 1) floor(log(n)/log(2)) - floor(log(1)/log(2))
                                           = sum_{n = 1}^(N + 1) floor(log(n)/log(2))
                                           = (N + 2)*floor(log_2(N + 1)) - 2*(2^floor(log_2(N + 1)) - 1)
    
    sum_{n = 1}^N val(n + 1,2) = sum_{n = 1}^(N + 1) val(n,2) - val(1, 2)
                               = sum_{n = 1}^(N + 1) val(n,2)
                               = N + 1 - bit cout of N + 1
    
Anwser:
    501985601490518144
--- 0.0 seconds ---
'''
import time, math
start_time = time.time()

def g(n, m):
    sm = bin(m).count("1")
    snm = bin(n-m).count("1")
    sn = bin(n).count("1")
    return sm + snm - sn

def val(n):
    return int(math.log(n - (n & n - 1), 2))

def F(n):
    return math.floor(math.log(n + 1, 2)) - val(n + 1)

def S(N):
    return (N + 2)*math.floor(math.log(N + 1, 2)) - 2*(pow(2, math.floor(math.log(N + 1, 2))) - 1) - (N + 1 - bin(N + 1).count("1"))


if __name__ == "__main__":
    print(S(10**16))
    print("--- %s seconds ---" % (time.time() - start_time))
