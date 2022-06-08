#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:28:53 2022

@author: igorvanloo
"""
'''
Project Euler Problem 309

https://en.wikipedia.org/wiki/Crossed_ladders_problem

Let 
A^2 + w^2 = y^2
B^2 + w^2 = x^2

Using pythagorean triples we can find triplets that have a matching w, but now we need to test if h is an integer

let w = w_1 + w_2 where it is divided where h meets w

We can see triangle BDA is a scaled up version of BEF and therefore h/w_1 = B/w
Similarly ACD is scaled up AEF => h/w_2 = A/w

Therefore w = w_1 + w_2 = hw/B + hw/A => 1 = h/B + h/A => AB = hA + hB => h = AB/(A + B)

Anwser:
    210139
--- 18.25213599205017 seconds ---
'''
import time, math
start_time = time.time()

def ppt(limit):  # Pythagorean Triplet generator
    triples = [[] for _ in range(limit + 1)]
    for m in range(2, int(math.sqrt(limit)) + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m ** 2 + n ** 2
                b = m ** 2 - n ** 2
                c = 2 * m * n
                if a < limit:
                    for k in range(1, limit // a + 1):
                        if k*a < limit:
                            triples[k*b].append(k*c)
                            triples[k*c].append(k*b)
    return triples

def compute(limit):
    triangles = ppt(limit)
    valid_triples = []
    for w in range(1, len(triangles)):
        possib = triangles[w]
        for y in range(len(possib)):
            A = possib[y]
            for x in range(y + 1, len(possib)):
                B = possib[x]
                if (A*B) % (A + B) == 0:
                    h = (A*B) // (A + B)
                    valid_triples.append(h) 
    return len(valid_triples)

if __name__ == "__main__":
    print(compute(1000000))
    print("--- %s seconds ---" % (time.time() - start_time))
