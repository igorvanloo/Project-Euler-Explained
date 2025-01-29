# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:31:58 2025

@author: Igor Van Loo
"""
'''
Project Euler Problem 142

1. a^2 = x + y
2. b^2 = x - y
3. c^2 = x + z
4. d^2 = x - z
5. e^2 = y + z
6. f^2 = y - z

7. 2x = x + y + x - y = a^2 + b^2
=> x = (a^2 + b^2)//2 
=> y = a^2 - x
=> z = c^2 - x

Then I just brute force

Answer:
    1006193
--- 14.715311050415039 seconds ---
'''
import time, math
start_time = time.time()

def is_sq(x):
    sqrt = (x ** (1 / 2))
    if round(sqrt) ** 2 == x:
        return True
    return False

def compute():
    
    for b in range(1, 1000):
        for a in range(b + 2, 1000, 2):
            x = (a*a + b*b)//2
            y = a*a - x
            if x < y:
                break
            else:
                for c in range(int(math.sqrt(x)), a):
                    z = c*c - x
                    if z > y:
                        break
                    else:
                        if all([is_sq(x - z), is_sq(y + z), is_sq(y - z)]):
                            #print(x, y, z)
                            return x + y + z

if __name__ == "__main__":
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
