# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:45:25 2023

@author: igorvanloo
"""
'''
Project Euler Problem 537

Find partitions of n, then for each partition calculate number of possibilities

for example T(3, 3)

3 = 3 + 0 + 0 = 2 + 1 + 0 = 1 + 1 + 1

1. 3 + 0 + 0
    There is only 1 number such that pi(n) = 0, that is n = 1
    There are 2 numbers such that pi(n) = 3, n = 5, 6
    Therefore we have 3!/2! * 2 = 6 different combinations of this form:
        (1,1,5), (1,5,1), (5,1,1), (1,1,6), (1,6,1), (6,1,1)

2. 2 + 1 + 0
    pi(n) = 0 => n = 1
    pi(n) = 1 => n = 2
    pi(n) = 2 => n = 3 or 4
    total 3!/(1! * 1! * 1!) * 2 = 12 combs of this form:
        (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1), (1,2,4), (1,4,2), (2,1,4), (2,4,1), (4,1,2), (4,2,1)

3. 1 + 1 + 1
    pi(n) = 1 => n = 2
    3!/3! * 1 = 1 comb of this form:
        (2, 2, 2)

Works but partitions are hard to generate, too slow. Need to think of another method

Notice that if a + b = k
let s = sum_{i = 1 to a} pi(x_i)
then n - s = sum_{i = a + 1 to k} pi(x_i)

so T(n, k) = sum_{s = 0 to n} T(s, a)T(n - s, b) - Convolution https://en.wikipedia.org/wiki/Convolution

Now T(n, 1) = number of numbers such that pi(x) = n we want to reduce T(n, k) into a sum and product of
T(n, 1)'s

T(3, 3) = sum_{s = 0 to 3} T(s, a)T(3 - s, b)
        = T(0, 1)T(3, 2) + T(1, 1)T(2, 2) + T(2, 1)T(1, 2) + T(3, 1)T(0, 2)
        
A = [T(0, 1), T(1, 1), T(2, 1), T(3, 1)]
B = [T(0, 2), T(1, 2), T(2, 2), T(3, 2)]

Then T(3, 3) = A[0]*B[3] + A[1]*B[2] + A[2]*B[1] + A[3]*B[0]

We know how to calculate A, how do we calculate B?

Then notice that
T(3, 2) = sum_{s = 0 to 3} T(s, a)T(3 - s, b)
        = T(0, 1)T(3, 1) + T(1, 1)T(2, 1) + T(2, 1)T(1, 1) + T(3, 1)T(0, 1)

T(2, 2) = sum_{s = 0 to 2} T(s, a)T(2 - s, b)
        = T(0, 1)T(2, 1) + T(1, 1)T(1, 1) + T(2, 1)T(0, 1)

T(1, 2) = sum_{s = 0 to 1} T(s, a)T(1 - s, b)
        = T(0, 1)T(1, 1) + T(1, 1)T(0, 1)
        
T(0, 2) = sum_{s = 0 to 1} T(s, a)T(1 - s, b)
        = T(0, 1)T(0, 1)

Clearly there is a pattern

the array [T(0, 2), T(1, 2), T(2, 2), T(3, 2)] can be generated through 
the array [T(0, 1), T(1, 1), T(2, 1), T(3, 1)] again!

Let let x = [T(0, 1), T(1, 1), T(2, 1), T(3, 1)]
For i in range(4):
    T(i, 2) = 0
    for j in range(i + 1):
        T(i, 2) += x[j]*x[i - j]
        
        #For example if i = 0, y = T(0, 2)
        #The for j in range(i + 1) only includes j = 0
        #So T(0, 2) = x[j]*x[i - j] = T(0, 1)T(0, 1) which is correct
        
So now we know how to generate any array of this form!

We just binary exponentiation to do it quickly and we are done

Anwser:
    779429131
--- 702.8318181037903 seconds ---
--- 32.04938626289368 seconds --- with pypy
'''
import time, math
start_time = time.time()
    
def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]
    
def T(n, k):
    mod = 1004535809
    primes = list_primes(300000)
    t1 = [1]
    for i in range(n + 1):
        t1.append(primes[i + 1] - primes[i])
    
    def conv(A, B):
        array = []
        for i, x in enumerate(A):
            t = 0
            for j in range(i + 1):
                t += A[j]*B[i - j]
                t %= mod
            array.append(t)
        return array
    
    res = [1]+[0]*(n)
    sq = t1
    while k != 0:
        print(k)
        if k % 2 != 0:
            res = conv(res, sq)
            k -= 1
        sq = conv(sq, sq)
        k //= 2
    return res[-1] % mod
    
if __name__ == "__main__":
    print(T(2*10**4, 2*10**4))
    print("--- %s seconds ---" % (time.time() - start_time))
