'''
Project Euler Problem 6

Anwser:
    25164150.0
--- 0.00011491775512695312 seconds ---
'''

import time

def compute(x):
    return abs(x*(x+1)*(-3*x**2 + x + 2)/12)

if __name__ == "__main__":
    start_time = time.time()
    print(compute(101))
    print("--- %s seconds ---" % (time.time() - start_time))
