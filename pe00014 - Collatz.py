#Euler Problem 14
#Collatz Sequence
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

def Collatz(n):
    count = 1
    while n != 1:
        if n % 2 ==0:
            n = n/2
            count = count + 1
        else:
            n = 3*n +1
            count = count + 1
    return count

def compute():
    ans = max(range(1, 1000000), key=Collatz)
    return ans
        
def Collatz1(x): #Slightly better code for collatz sequence 
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = 3 * x + 1
    return Collatz1(y) + 1        
    

    