'''
Project Euler Problem 10

Anwser:
    142913828922
--- 0.3636751174926758 seconds ---
'''

import time, math

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

def list_primes(n):
	return sum([i for (i, isprime) in enumerate(list_primality(n)) if isprime])

if __name__ == "__main__":
    start_time = time.time()
    print(list_primes(2000000))
    print("--- %s seconds ---" % (time.time() - start_time))




