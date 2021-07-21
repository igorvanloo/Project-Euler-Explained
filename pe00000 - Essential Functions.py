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

def ReadFile(): #Create the inital list 
    file = open("Input File name")
    data = file.readlines()
    file.close()
    datalist = []
    for x in data:
        x = x.rstrip()
        datalist.append(x)
    return datalist

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

def primefactorization(n, listofprimes): #Requires a preloaded list of primes
    if is_prime(n) == True:
        return [n]
    else:
        factors = []
        while n != 1:
            for x in listofprimes:
                if n % x == 0:
                    factors.append(x)
                    n = n/x
                    break
        return factors
    
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
                factors.append(n)
            break
    return factors

def factorial(x): #Factorial function we can just use math.factorial
    total = 1
    if x == 0:
        return total
    else:
        for y in range(1,x+1):
            total *= y
        return total
    
def base2converter(x): #Simple base 2 converter we can also use bin function
    if x < 0:
        return "Wrong input"
    base2version = ""
    while x > 0:
        temp = x % 2
        base2version += str(int(temp))
        x = (x - int(temp))/2
    return base2version[::-1]

def n_choose_r(n, r): #nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def permutations(number): #Returns list containing strings of permutations, can be edited to suit need
    final_list = []
    string = str(number)
    temp_permutations = list(itertools.permutations(string))
    for y in range(len(temp_permutations)):
            temp_var = "".join(str(temp_permutations[y][i]) for i in range(len(temp_permutations[y])))
            final_list.append(temp_var)
            
    return final_list

def is_quadratic(x):
    cube__root = (x**(1/2))
    if round(cube__root) ** 2 == x:
        return True
    return False

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

def overall_fraction(cf): #Returns the fractional form of the canonical form
    numerator = 1
    denominator = cf[0]
    
    for x in range(1,len(cf)):
        denominator, numerator =cf[x]*denominator + numerator, denominator
                
    return denominator, numerator

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

def Fibtill(x):
    fibnumbers = []
    n = 1
    while fibonnaci(n) <= x:
        fibnumbers.append(fibonnaci(n))
        n += 1
    return fibnumbers
    
def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    divisors.remove(x)
    return (divisors)
   
def phi(n, primes): #Eulers Totient Function requires primefactorization and isprime function
    total = n
    prime_factor = primefactorization(n, primes)
    
    for p in prime_factor:
        total *= (1-1/p)
        
    return int(total)

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

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

def ZeckendorfRepresentation(x, fibnumbers): #Returns list with zeckendorf decomposition, requires a list of fibonnaci numbers
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

def ppt(limit): #Pythagorean Triplet generator
    triples = []
    for m in range(2,int(math.sqrt(1000))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                
                p = max(a,b,c)
                
                for k in range(1,int(limit/p)+1):
                    triples.append([k*b,k*c,k*a])
    return triples
