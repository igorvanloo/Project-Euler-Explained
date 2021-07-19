'''
Project Euler Problem 7

Anwser:
    104743
--- 0.17671489715576172 seconds ---
    
'''

import time, math, eulerlib

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

def compute(x):
    temp = list_primes(10**6)
    return temp[x-1]

if __name__ == "__main__":
    start_time = time.time()
    print(compute(10001))
    print("--- %s seconds ---" % (time.time() - start_time))