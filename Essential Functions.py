"""
@author: igorvanloo
"""
'''
Project Euler Essential Functions

See https://mathslib.readthedocs.io/en/latest/ for full documentation on all the functions
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

def fibonacci(n): #Finds the nth fibonacci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

#Fins the nth fibonacci number, using fast exponentiation
#------------------------------------------------------------------------------------------------------------------#

def Fibtill(x):
    fibnumbers = []
    n = 1
    while fibonacci(n) <= x:
        fibnumbers.append(fibonacci(n))
        n += 1
    return fibnumbers

#Additional function for fibonacci(n) to find all fibonacci numbers up till x
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
    prime_fac = {}
    for y in primes:
        total = 0
        for i in range(1, int(math.floor(math.log(x,y))) + 1):
            total += int(math.floor(x/(y**i)))
        prime_fac[y] = total
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
    try:
        inv = pow(b,-1,m)
    except ValueError:
        return "Division not defined"
    else:
        return (inv*a) % m

#Performs Modular Division where a/b mod(m)
#------------------------------------------------------------------------------------------------------------------#

def k_smooth_numbers(max_prime, limit):
    k_s_n = [1]
    p = list_primes(max_prime)
    while len(p) != 0:
        temp_k_s_n = []
        curr_p = p.pop(0)
        power_limit = int(math.log(limit, curr_p)) + 1
        curr_multiples = [curr_p**x for x in range(1, power_limit + 1)]
        for x in curr_multiples:
            for y in k_s_n:
                temp = x*y
                if temp <= limit:
                    temp_k_s_n.append(temp)
        k_s_n += temp_k_s_n
    return len(k_s_n)

#Finds all k-smooth numbers ≤ limit where k = max_prime 
#------------------------------------------------------------------------------------------------------------------#

def legendre_symbol(a, p):
    t = pow(a, (p-1)//2, p)
    if t == p - 1:
        return -1
    return t

#Returns the legendre symbol of a/p: 
# 1 if a is a quadratic residue modulo p and p does not divide a
# -1 if a is a non-quadratic residue modulo p
# 0 if p divides a
#------------------------------------------------------------------------------------------------------------------#

def tonelli_shanks(a, p):
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1)//4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    s = int(s)
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1)//2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e
    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)
        if m == 0:
            return x
        gs = pow(g, 2**(r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

#Implementation of the Tonelli-Shanks Algorithm full credit goes to: 
#https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/
#------------------------------------------------------------------------------------------------------------------#

def PrimsAlgorithm(graph):
    dimension = len(graph)
    Previous_Weight = sum([graph[x][y] for x in range(dimension) for y in range(x+1, dimension) if graph[x][y] != 0])
    Tree = set([0])
    New_Weight = 0    
    for x in range(dimension - 1):
        Minimum_edge, Corresponding_vertex = min([(graph[x][y], y) for x in Tree for y in range(dimension) if y not in Tree and graph[x][y] != 0])
        Tree.add(Corresponding_vertex)
        New_Weight += Minimum_edge
        if len(Tree) == dimension:
            break
    return Previous_Weight - New_Weight

#My own implementation of Prim's Algorithm. Used to find Minimum Spanning Tree for weighted undirected graph
#------------------------------------------------------------------------------------------------------------------#

def DijkstrasAlgorithm(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    INF = 10**8    
    unvisisted_nodes = dict()
    for x in range(rows):
        for y in range(columns):
            unvisisted_nodes[(x, y)] = INF
    unvisisted_nodes[(0, 0)] = matrix[0][0]    
    mask = [[INF]*columns for i in range(rows)]
    mask[0][0] = matrix[0][0]    
    def visit_neighbour(og_x, og_y, x, y, unvisisted_nodes):
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return False
        if (x, y) in unvisisted_nodes:
            return min(mask[x][y], mask[og_x][og_y] + matrix[x][y])
    curr = (0, 0) #Starting node
    while True:
        x, y = curr
        for (a, b) in ((x + 1, y), (x, y+ 1), (x - 1, y), (x, y - 1)):
            temp = visit_neighbour(x, y, a, b, unvisisted_nodes)
            if temp:
                mask[a][b] = temp
                unvisisted_nodes[(a, b)] = temp
        unvisisted_nodes.pop(curr)        
        if len(unvisisted_nodes) != 0:
            curr = min(unvisisted_nodes, key=unvisisted_nodes.get)
        else:
            break
    return mask[rows - 1][columns - 1] #Ending node

#My own implementation of Dijkstra's Algorithm. Used to find shortest path between nodes in a graph
#------------------------------------------------------------------------------------------------------------------#

def ChineseRemainderTheorem(a1, a2, n1, n2):
    if a1 > n1 or a2 > n2:
        return "Wrong values were input"
    #x = a1 (mod n1)
    #x = a2 (mod n2)
    #We find p = n1^-1 (mod n2), q = n2^-1 (mod n1)
    p, q = pow(n1, -1, n2), pow(n2, -1, n1)
    #The unique solution to this system is a1*q*n2 + a2*p*n1 % n1*n2
    return (a1*q*n2+ a2*p*n1) % (n1*n2)

#Simple Chinese Remiander Theorem to solve x = a1 mod n1, x = a2 mod n2
#------------------------------------------------------------------------------------------------------------------#

def FrobeniusNumber(*integers):
    #Set is first sorted
    A = sorted(integers)
    #Initalize n value for future reference
    n = len(A) 
    #Initalize a1 and an for readability
    a1 = A[0]
    an = A[n - 1]
    #Step 1
    #Initalize FIFO queue
    Q = [0]
    #Initalize P
    P = [0]*a1
    P[0] = n
    #Initalize S, label vector, in which each currently known minimal path weight to a vertex is stored.
    S = [a1*an]*a1
    S[0] = 0
    #initalize Amod
    Amod = [a % a1 for a in A]
    #Step 2
    while len(Q) != 0:
        #Step 2a
        v = Q.pop(0) #Remove the head of Q and set it to the vertex v
        #Step 2b
        for j in range(2, P[v] + 1):
            #Step 2bi
            u = v + Amod[j - 1]
            if u >= a1:
                u -= a1
            #Step 2bii
            w = S[v] + A[j - 1]
            #Step 2biii
            if w < S[u]:
                S[u] = w
                P[u] = j
                if u not in Q:
                    Q.append(u)
    #Step 3
    return max(S) - a1

#Finds the Frobenius number of a set of integers
#------------------------------------------------------------------------------------------------------------------#

def miller_rabin(n, milleronly = True, numoftests = 0):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    
    if milleronly:
        if n < 1373653:
            tests = [2, 3]
        elif n < 9080191:
            tests = [31, 73]
        elif n < 25326001:
            tests = [2, 3, 5]
        elif n < 4759123141:
            tests = [2, 7, 61]
        elif n < 2152302898747:
            tests = [2, 3, 5, 7, 11]
        elif n < 3474749660383:
            tests = [2, 3, 5, 7, 11, 13]
        elif n < 341550071728321:
            tests = [2, 3, 5, 7, 11, 13, 17]
        elif n < 3825123056546413051:
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        elif n < 318665857834031151167461: # < 2^64
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        elif n < 3317044064679887385961981:
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        else:
            tests = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    else:
        from random import randrange
        numoftests %= n
        tests = [randrange(2, n) for _ in range(numoftests)]
        
    d = n - 1
    r = 0
    
    while d % 2 == 0:
        d //= 2
        r += 1
    
    def is_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(r):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True
    
    for k in tests:
        if is_composite(k):
            return False
    return True

#Implementation of Rabin-Miller primality test with the option to use the Miller test
#------------------------------------------------------------------------------------------------------------------#



