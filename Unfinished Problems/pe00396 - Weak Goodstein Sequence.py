# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:27:37 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 396

https://www.youtube.com/watch?v=Y-4h01oTROw

https://en.wikipedia.org/wiki/Goodstein%27s_theorem

Answer:
    173214653
'''
import time, math
start_time = time.time()

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits

def basetoNumber(n, b):
    return sum(x*b**i for i, x in enumerate(n))

def g(n):
    g1 = n

    g_list = [g1]
    k = 2
    while g1 != 0:
        #print(math.log(g1, k), k)
        v = numberToBase(g1, k)
        g1 = basetoNumber(v, k + 1) - 1
        k += 1 
        g_list.append(g1)
        
    return len(g_list) - 1

def g2(n, mod):
    t = 1
    v = numberToBase(n, 2)
    while True:
        
        l = len(v)
        if l == 1:
            break
        
        for i in range(1, l):
            if v[i] != 0:
                t += (v[0] + 1) % mod
                
                v[i] -= 1
                if v[i] == 0:
                    
                    if i == len(v) - 1:
                        v.pop(-1)

                    for j in range(i):
                        v[j] = t % mod
                    print(v)
                    break
                else:
                    if i == 2:
                        a = 2*v[0] + 2
                        v[0] = (v[0] + 1)*pow(2, a, mod) - 1
                    else:
                        v[0] += (v[0] + 1) % mod

                    break
        v[0] %= mod
    return (t + v[0] - 1) % mod


def compute(n):
    mod = 10**9
    return sum(g2(i, mod) for i in range(1, n)) % mod

if __name__ == "__main__":
    print(compute(8))
    print("--- %s seconds ---" % (time.time() - start_time))
