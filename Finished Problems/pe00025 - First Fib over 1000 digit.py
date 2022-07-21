'''
Project Euler Problem 25

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Answer:
    
'''
import time

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

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
    fib = [1,1,2]
    fn = 2
    while len(str(fn)) != 2000:
        fn = fib[-1] + fib[-2]
        fib.append(fn)
    return len(fib)

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))