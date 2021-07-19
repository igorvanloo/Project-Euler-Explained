#Euler Problem 26
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions 
with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
#The basis of this proof is that all nonprimes intergers can be made as a product of other integers
#Similarly the recurring decimals will be the same for example 1/126 = 1/7 * 1/6 * 1/3 recurring decimal is still 6
#Therefore we will look for the recurring decimals of all the primes numbers 

def primestill1000(): #We define all our primes till 1000, omit 2 and 5 as they are not necessary
    primes = []
    for i in range(3,1001,2):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    primes.remove(5)
    return primes

#From fermats little theorem the recurring decimal length is equal to the order of 10 modulo p
#This means that 10^x congruent to 1 mod p, x is our recurring decimal length
#So we iterature from x: 1 till p-1, on 10^x once 10^x mod p = 1 we stop and return that length                
def lengthofdecimal(x): 
    for i in range(1,x):
        if (10**i) % x == 1:
            return i
            break

#Lastly we create a dictionary so that we can add which prime corresponds to which length
#We return the key (In this case the prime) which corresponds to the maximum length value        
def compute():
    allprimes = primestill1000()
    dict1 = {}
    for i in range(len(allprimes)):
        length = lengthofdecimal(allprimes[i])
        dict1[allprimes[i]]=length
    return max(dict1, key=dict1.get)

print(compute())
        

