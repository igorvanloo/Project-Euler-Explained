#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:51:18 2020

@author: igorvanloo
"""
'''
Project Euler Essential Functions
'''

import math

#------------------------------------------------------------------------------------------------------------------#
def ReadFile(): #Create the inital list 
    file = open("Input File name")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        datalist.append(x)
    return datalist

#------------------------------------------------------------------------------------------------------------------#

def Prime_sieve(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

#Returns a list containing True or False, list[x] = True => x is a prime
#------------------------------------------------------------------------------------------------------------------#

def list_primes(n):
	return [i for (i, isprime) in enumerate(Prime_sieve(n)) if isprime]

#Converts list above to a list of primes
#------------------------------------------------------------------------------------------------------------------#

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

#is_prime function, checks if a number if prime
#------------------------------------------------------------------------------------------------------------------#
    
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(int(n))
            break
    return factors

def prime_factors_with_exponent(n):
    factors = []
    d = 2
    while n > 1:
        count = 0
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            factors.append([d, count])
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append([int(n),1])
            break
    return factors

#Prime factorisation function's, with or without exponent's
#------------------------------------------------------------------------------------------------------------------#

def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    divisors.remove(x)
    return (divisors)

#Find all divisors of a number x
#------------------------------------------------------------------------------------------------------------------#

def n_choose_r(n, r): #nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

#Simple n C r function
#------------------------------------------------------------------------------------------------------------------#

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

#Base changing function, number = n, base = b
#------------------------------------------------------------------------------------------------------------------#

def is_square(x):
    square_root = (x**(1/2))
    if round(square_root) ** 2 == x:
        return True
    return False

#Simple is square number function
#------------------------------------------------------------------------------------------------------------------#

def continued_fraction(x):
    m0 = 0
    d0 = 1
    a0 = math.floor(math.sqrt(x)) #These are the starting values
    temp_list = [a0]
    while True:
        mn = int(d0*a0 - m0) 
        dn = int((x - mn**2)/d0)
        an = int(math.floor((math.sqrt(x) + mn) / dn)) #new values
        temp_list.append(an)
        #if an == 2*math.floor(math.sqrt(x)):
            #break
        if len(temp_list) == 100:
            break
        m0 = mn
        d0 = dn
        a0 = an #Replace values
    return temp_list

#Returns the continued fraction of sqrt(x) 
#------------------------------------------------------------------------------------------------------------------#

def overall_fraction(cf): 
    numerator = 1
    denominator = cf[0]
    
    for x in range(1,len(cf)):
        denominator, numerator =cf[x]*denominator + numerator, denominator
                
    return denominator, numerator

#Returns the fractional form of the continued fraction
#------------------------------------------------------------------------------------------------------------------#

def fibonacci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

#Fins the nth fibonnaci number, using fast exponentiation
#------------------------------------------------------------------------------------------------------------------#

def Fibtill(x):
    fibnumbers = []
    n = 1
    while fibonacci(n) <= x:
        fibnumbers.append(fibonacci(n))
        n += 1
    return fibnumbers

#Additional function for fibonnaci(n) to find all fibonacci numbers up till x
#------------------------------------------------------------------------------------------------------------------#

def phi(n):
    if n == 1:
        return 1
    phi = 1
    d = 2 
    while n > 1:
        count = 0 
        while n % d == 0:
            count += 1
            n /= d
        if count > 0:
            phi *= (d**(count-1))*(d-1)
        d = d + 1
        if d*d > n:
            if n > 1: 
                phi *= int(n - 1)
            break
    return phi

#Eulers Totient Function counts the positive integers up to a given integer n that are relatively prime to n
#------------------------------------------------------------------------------------------------------------------#

def Mobius(n):
    if n == 1:
        return 1
    d = 2
    num_of_primes = 0
    while n > 1:
        while n % d == 0:
            num_of_primes += 1
            if n % (d*d) == 0:
                return 0
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                num_of_primes += 1
            break
    return (-1)**num_of_primes

#Mobius function, returns 0 if n is divisible by p^2, otherwise returns (-1)^k, where k is number of distinct prime factors
#------------------------------------------------------------------------------------------------------------------#

def partition(k,n): #Partition function, fast up till n = 85 works with sum of partition function
    if k == 0 and n == 0:
        return 1
    elif k <= 0 or n <= 0:
        return 0
    return partition(k, n-k) + partition(k-1, n-1)

def Partition(goal, alist):
    ways = [1] * (goal+1)
    for options in alist:
        for i in range(len(ways) - options):
            ways[i + options] += ways[i]
    return ways[-1]-1  

#First function uses mathematical recursion equation, it is extremely slow
#Second function uses dynamic programming, it is very quick
#------------------------------------------------------------------------------------------------------------------#

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

#Simple sum of digits function
#------------------------------------------------------------------------------------------------------------------#

def ZeckendorfRepresentation(x, fibnumbers): 
    rep = []
    number = x
    count = 0
    while number != 0:
        
        if number - fibnumbers[count] >= 0:
            number -= fibnumbers[count]
            rep.append(fibnumbers[count])
            count += 1
        count += 1
        
    return rep

#Returns list with zeckendorf decomposition, requires a list of fibonnaci numbers
#------------------------------------------------------------------------------------------------------------------#

def ppt(limit): 
    triples = []
    for m in range(2,int(math.sqrt(limit))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                
                p = max(a,b,c)
                
                for k in range(1,int(limit/p)+1):
                    triples.append([k*b,k*c,k*a])
    return triples

#Pythagorean Triplet generator
#------------------------------------------------------------------------------------------------------------------#

def lcm(a_list):
    n = sorted(a_list)
    curr = n.pop(-1)
    while len(n) != 0:
        temp = n.pop(-1)
        curr = int(abs(curr*temp)/math.gcd(curr, temp))
    return curr

#Takes a list of numbers and returns the lcm of all numbers
#------------------------------------------------------------------------------------------------------------------#

def legendre_factorial(x):
    primes = list_primes(x)
    prime_fac = []
    for y in primes:
        total = 0
        for i in range(1, int(math.floor(math.log(x,y))) + 1):
            total += int(math.floor(x/(y**i)))
        prime_fac.append([y, total])
    return prime_fac

#Calculates the prime factorisation of massive factorials
#------------------------------------------------------------------------------------------------------------------#

def primepi(limit): 
    prime_gen = Prime_sieve(limit + 50)
    primes = [x for x in range(len(prime_gen)) if prime_gen[x]]
    array = [0]*(limit+1)
    p_index = 0
    for x in range(1, limit + 1):
        while True:
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    return array

#Returns an array such that array[x] = number of primes < x (this is commonly known as primepi)
#------------------------------------------------------------------------------------------------------------------#

def ModDivision(a,b,m):
    a = a % m
    inv = pow(b,-1,m)
    if inv == -1:
        return "Division not defined"
    else:
        return (inv*a) % m

#Performs Modular Division where a/b mod(m)
#------------------------------------------------------------------------------------------------------------------#