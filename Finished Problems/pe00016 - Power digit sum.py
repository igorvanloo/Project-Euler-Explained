'''
Project Euler Problem 16

Anwser:
    1366
--- 0.00029397010803222656 seconds ---
    
'''

import time, math

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

if __name__ == "__main__":
    start_time = time.time()
    print(sum_digits(2**1000))
    print("--- %s seconds ---" % (time.time() - start_time))



