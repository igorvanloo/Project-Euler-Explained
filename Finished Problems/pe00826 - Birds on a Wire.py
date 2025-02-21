# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:10:50 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 826

Approximation with 10^7 trials using fractions limit_denominator method

n   |   decimal     |   limit_denominator(1000)     |   limit_denominator(100)
(4, 0.4778826480110296, Fraction(443, 927), Fraction(43, 90))
(5, 0.4629744838024842, Fraction(444, 959), Fraction(25, 54))
(6, 0.45250030742527514, Fraction(181, 400), Fraction(19, 42))
(7, 0.44441246633003195, Fraction(4, 9), Fraction(4, 9))
(8, 0.43824781124413786, Fraction(110, 251), Fraction(39, 89))

Approximation with 10^8 trials using fractions limit_denominator method

n   |   decimal     |   limit_denominator(1000)     |   limit_denominator(100)
(4, 0.4777621850553789, Fraction(333, 697), Fraction(43, 90))
(5, 0.4629255090526395, Fraction(231, 499), Fraction(25, 54))
(6, 0.45235191723847484, Fraction(375, 829), Fraction(19, 42))
(7, 0.44449001554067075, Fraction(4, 9), Fraction(4, 9))
(8, 0.43828522131966563, Fraction(419, 956), Fraction(32, 73))

Using first 4 digits and plugging into wolfram alpha and we get matching cases

n = 3: 0.4999(373477655839) ~ 1/2
n = 4: 0.4777(7858255956557) ~ 32/67 (although another 7 seems likely, then we get ~ 43/90)
n = 5: 0.4629(179637555979) ~ 25/54
n = 6: 0.4523(231596394622) ~ 19/42
n = 7: 0.4444456786389037 ~ 4/9
n = 8: 0.4381287272417751 ~ ?

For a massive amount of birds it seems to be convergeing to 0.388888 ~ 7/18
n = 1,000: 0.3891118158078133, Fraction(193, 496), Fraction(7, 18), 10,000 trials
n = 10,000: 0.38893046519289154, Fraction(387, 995), Fraction(7, 18), 10,000 trials
n = 100,000: 0.3888896339813669, Fraction(7, 18), Fraction(7, 18), 1,000 trials
n = 1,000,000: 0.3888891119536712, Fraction(7, 18), Fraction(7, 18), 100 trials

Conjecture: painted amount is (7n + a)/(18n + b) comparing first 2 values we get a = 15, b = 18

Answer:
    0.3889014797
--- 0.25379228591918945 seconds ---
'''
import time, math
import random
import fractions
start_time = time.time()

def monte_carlo(trials, n):
    total = 0
    for _ in range(trials):
        painted = 0
        pts = sorted([random.random() for _ in range(n)])
        prev = 1
        for i, x in enumerate(pts):
            if i == 0:
                painted += pts[i + 1] - x
            elif i == (n - 1):
                if prev == 0:
                    painted += x - pts[i - 1]
            else:
                v = [x - pts[i - 1], pts[i + 1] - x]
                if v[1] > v[0]:
                    curr = 0
                else:
                    curr = 1
                    
                if prev != 1 or curr != 0:
                    painted += v[curr]
                prev = curr
        total += painted
    return n, total/trials, fractions.Fraction(total / trials).limit_denominator(1000), fractions.Fraction(total / trials).limit_denominator(100)
    
def F(n):
    num = 7*n + 15
    den = 18*(n + 1)
    #g = math.gcd(num, den)
    return round(num/den, 15)

def prime_sieve(limit, values = True):
    result = [True] * (limit + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(limit)) + 1):
    	if result[i]:
    		for j in range(2 * i, len(result), i):
    			result[j] = False
    if values:
        return [i for (i, isprime) in enumerate(result) if isprime]
    else:
        return result
    
def compute(n):
    primes = prime_sieve(n)
    l = len(primes) - 1
    total = 0
    for p in primes[1:]:
        total += F(p)
    return round(total/l, 10)
            
if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
