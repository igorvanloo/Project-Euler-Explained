#Project Euler 20
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

#math.factorial() #This is predefined factorial function 

def factorial(x): #Self created
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact

def sumofdigit(x):
    number = str(factorial(x))
    total = 0
    for i in number:
        total = total + int(i)
    return total

print(sumofdigit(100))