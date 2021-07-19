#Euler Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

n = 9827342304 # Number we are testing
'''
primes = [2] #This will add a list of all the prime factors we need to check later
for x in range(3,int(math.sqrt(n)+1),2):
    if sum([float(x/y).is_integer() for y in range (3,int(math.sqrt(x)+1),2)])==0:
        primes.append(x)
print(primes)
'''
import eulerlib, math

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
    
def prime_factors1(n):
    primes = [2] #This will add a list of all the prime factors we need to check later
    for x in range(3,int(math.sqrt(n)+1),2):
        test = True
        for y in range (3,int(math.sqrt(x)+1),2):
            if float(x/y).is_integer():
                test = False
                break
        if test == True:
            primes.append(x)
     
    factors = [] #This will add a list of all the prime factors and the remainder if there is
    while n != 1:
        for i in range(len(primes)-1,-1,-1): #Now we test for the prime factorization 
            if n % int(primes[i]) == 0:
                factors.append(int(primes[i])) #adding prime factors to list otherwise just pass
                n = n / int(primes[i]) #resetting n to test for next smallest prime factors
    return factors

def prime_factors(n):
    if is_prime(n) == True:
        return [n]
    primes = eulerlib.primes(int(math.sqrt(n)+1))
     
    factors = [] #This will add a list of all the prime factors and the remainder if there is
    while n != 1:
        for i in range(len(primes)-1,-1,-1): #Now we test for the prime factorization 
            if n % int(primes[i]) == 0:
                factors.append(int(primes[i])) #adding prime factors to list otherwise just pass
                n = n / int(primes[i]) #resetting n to test for next smallest prime factors
    return factors