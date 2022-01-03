'''
Project Euler Problem 27

Find a quadratic x^2+ax+b, |a| < 1000, |b| <= 1000 that produces the most primes in a row starting at x = 0
Then find the product ab

b must be prime, we can limit the search of a because when x = 1, 1 + a + b must be prime => a > b-1

Answer:
    (71, -59231)
--- 0.31620097160339355 seconds ---   
'''

import eulerlib, time, math

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

def is_prime(x): #Test if giving value is a prime 
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True
    
def function(a, b):
    count = 0
    x = 0
    while True:
        if is_prime((x*x)+a*x+b):
            count += 1
            x += 1
        else:
            break
    return count

def compute():
    maximum = 1
    maxnums = 1
    for b in list_primes(1000):
        for a in range(1-b, 1000):
            if is_prime(a+b+1):
                temp = function(a,b)
                if temp > maximum:
                    maximum = temp
                    maxnums = a*b
                    
    return maximum, maxnums
    
if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))