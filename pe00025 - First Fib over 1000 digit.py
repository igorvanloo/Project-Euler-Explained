#Project Euler Problem 25
'''
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

def Fibonnaci(x):
    fibnumbers = [1,1]
    f1 = 1
    f2 = 1
    while len(fibnumbers) != x:
        fx = f2 + f1
        fibnumbers.append(fx)
        f1 = f2
        f2 = fx
    return fibnumbers

def compute():
    x = 3
    fib = Fibonnaci(x)
    while len(str(fib[-1])) != 1000:
        x = x + 1
        fib = Fibonnaci(x)
    return len(fib)

print(compute())