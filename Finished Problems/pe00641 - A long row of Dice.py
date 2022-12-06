# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:19:54 2022

@author: igorvanloo
"""
'''
Project Euler Problem 641

start with a row of n dice showing 1,
increase every dice divisible by 2 by 1
increase every dice divisible by 3 by 1
increase every dice divisible by 4 = 2^2 by 1
...
increase every dice divisible by n by 1

if a dice shows 6 and is increased it is reverted to 1
f(n) = #of dice showing a 1 after the process
f(100) = 2
f(10^8) = 69

It is easy enough to see that the nth dice will show σ_0(n) without subtracting 6, 
that is the nth dice will show the number of divisors it has

Therefore the problem is asking how many k are there such that k <= n and σ_0(k) = 1 mod (6)

σ_0(k) = prod_{i = 1 to r} (e_i + 1) where k = p_1^e_1...p_r^e_r

We need σ_0(k) to first of all be odd, therefore e_i cannot be odd, since then e_i + 1 = 2l and then σ_0(k) will be even

e_i cannot be odd means that e_i is even therefore e_i = 2a_i and hence k must be a perfect square

Given n, we can construct a sieve of length sqrt(n), array, 
and then for each prime p|x multiply array[x] *= (2*c + 1) where x = p^c * k where p does not divide k
This way we directly compute the number of divisors of perfect squares, like this we get f(10^14) in 12 seconds

Investigating the actual numbers such that σ_0(k) = 1 (mod 6) I can see that the prime factorizations
always have order have some patterns, most importantly every k will have a prime factor with exponenent >= 4
Why?
Suppose k = p^2 * k_1 where p does not divide k_1 then σ_0(k) = 3σ_0(k_1) 
we then require 3σ_0(k_1) = 1 (mod 6) which has no solutions! therefore we need only primes <= n^(1/4)

I also notice, and it is clear that if k = p^l then σ_0(k) = l + 1 and therefore 6|l (then σ_0(k) = 1 (mod 6))
so our largest solo prime must be less than n^(1/6)

Take the largest prime possible p, then minimally k = p^4 * k_1 where p does not divide k_1
σ_0(k) = 5σ_0(k_1) therefore we require σ_0(k_1) = 5l => we have another prime factor with exponenent 4,
the smallest such is 2, therefore our largest prime factor possible is n^(1/4)/2

Furthermore, all our prime exponenents are even, therefore all of our contributions are odd as needed
if we have 
1. σ_0(k) = l, that is, we have a prime with exponent 6k + 1, then we only have l = 1 (mod 6) if l = 6k + 1
    l = 6k + 1 => we have a prime factor with exponent = 6k
    
2. σ_0(k) = 3l, then 3l = 1 (mod 6) has no solutions

3. σ_0(k) = 5l, then 5l = 1 (mod 6) only has a solution if l = 6k + 5
    l = 6k + 5 => we have a prime factor with exponent = 6k + 4
    
We can also notice that if we have a prime factor with exponenent of the form 6k + 4, we need another one!
All of our numbers are represented as n = a^6 * b^4

    f(10**24) = 788749
--- 2.7125816345214844 seconds ---
    f(10**28) = 7915837
--- 23.336220502853394 seconds ---
    f(10**30) = 25055676
--- 72.42807674407959 seconds ---
    f(10**32) = 79290673
--- 237.00297570228577 seconds ---

Anwser:
    793525366
--- 2328.9859478473663 seconds ---
'''
import time, math
start_time = time.time() 

def Segmented_Prime_Sieve(limit, block_size = 0):
    primes = []
    sqrtN = int(math.sqrt(limit))
    result = [True]*(sqrtN + 2)
    for i in range(2, sqrtN + 1):
        if result[i]:
            primes.append(i)
            for j in range(2*i, sqrtN + 1, i):
                result[j] = False
    
    #Now we have generated all primes under sqrt(n), this is all we need to mark the other primes
    all_primes = []
    marker = [0]*len(primes)
    
    if block_size == 0:
        block_size = sqrtN
        
    for k in range(1, limit//block_size):
        if k % 100 == 0:
            print("%s percent done" % (k/(limit//block_size)))
        block_start = k*block_size + 1
        block_end = (k + 1)*block_size
        curr_result = [True]*block_size
        
        if k == 1:
            for p_index, p in enumerate(primes):
                count = 0
                while (block_start + count) % p != 0:
                    count += 1
                
                for j in range(block_start + count, block_end + 1, p):
                    curr_result[j - block_start] = False
                    marker[p_index] = j
        else:
            for p_index, p in enumerate(primes):
                for j in range(marker[p_index] + p, block_end + 1, p):
                    curr_result[j - block_start] = False
                    marker[p_index] = j
        
        all_primes += [block_start + i for (i, isprime) in enumerate(curr_result) if isprime]
    
    return primes + all_primes

def f(n):
    upper_bound = int((n**(1/4))/2) + 20000
    primes = Segmented_Prime_Sieve(upper_bound) 
    print("Primes Generated")
    print("--- %s seconds ---" % (time.time() - start_time))

    l = len(primes)
    
    def generate(curr, primeIndex, needAnotherPF4):
        # Depending on needAnotherPF4 we have found a candidate
        if needAnotherPF4:
            total = 0
        else:
            total = 1
        # Now we go through all of the future primes
        for i in range(primeIndex, l):
            p = primes[i]
            # If needAnotherPF4 then we set exp to 4, else 6
            if needAnotherPF4:
                exp = 4
            else:
                exp = 6
                
            if curr*pow(p, exp) > n:
                break
            # Go through every exponent which is a multiple of 6, that is Case 1
            else:
                t = 6
                while True:
                    v = curr*pow(p, t)
                    if v > n:
                        break
                    # We continue the process with the next prime, and we keep the status of needAnotherPF4
                    total += generate(v, i + 1, needAnotherPF4)
                    t += 6
                # Go through every exponent which is a multiple of 6, that is Case 3
                t = 4
                while True:
                    v = curr*pow(p, t)
                    if v > n:
                        break
                    # We continue the process with the next prime, and we keep the change the status of
                    # needAnotherPF4 because we've added a prime factor with exponent 4
                    total += generate(v, i + 1, not needAnotherPF4)
                    t += 6
        return total
            
    return generate(1, 0, False)

if __name__ == "__main__":
    print(f(10**36))
    print("--- %s seconds ---" % (time.time() - start_time))

