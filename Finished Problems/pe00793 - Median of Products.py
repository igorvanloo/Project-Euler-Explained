'''
Project Euler Problem 793

Instead of directly calculating the median by listing all elements (would take n^2 time), we do something smarter.

1. First lets sort the set S = {S_0, ... S_{n-1}}

2. Using a binary search let low = S_0*S_1, high = S_{n-2}*S_{n-1}, and m be the middle value, let this m
be our intital guess for the median

    2.1. There are going to be nC2 = n(n - 1)/2 pairwise products and therefore if there are n(n-1)/4 products which are 
    less than m, then m is the median of this set by definition.

    2.2. Therefore, we need loop through the set S only once, which is the crucial part to lower the time complexity,
    Let say we are on element S_i, then we find the maximal element, j, such that S_i*S_j ≤ m, we can do this with
    a binary search again in S by using m/S_i
    
        2.2.1 Once we have found j, it means that there will be j - i products which do not exceed m becuase we must
        have that i < j by the problem definition

    2.3 Once we have found the total products less than m, if the number is greater than our goal (n(n-1)/4), then
    we know that this guess is too high, we let high = mid - 1, otherwise, if we have too little then let lo = mid

3. After the binary search we will have found our median

Anwser:
    475808650131120
--- 18.502281427383423 seconds ---
'''
import time
from bisect import bisect_right
start_time = time.time()

def bisect(alist, goal):
    #Equivalent to bisect_right from bisect module
    lo = 0
    hi = len(alist)
    while lo < hi:
        mid = (lo + hi)//2
        if goal < alist[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def s(n):
    s0 = 290797
    array = []
    for _ in range(n):
        array.append(s0)
        s0 = (s0*s0) % 50515093
    return sorted(array)

def compute(n):
    S = s(n)
    lo, hi = S[0]*S[1], S[-1]*S[-2]
    goal = (n*(n-1))//4
    while lo < hi - 1:
        mid = (lo + hi)//2
        products = 0
        for i, x in enumerate(S):
            if x * x > mid:
                break
            #j = bisect(S, mid//x) #This method is about 5x slower
            j = bisect_right(S, mid//x) #Use C implementation for speed up 
            if j > i:
                products += j - i - 1
        if products > goal:
            hi = mid
        else:
            lo = mid
    return hi

if __name__ == "__main__":
    print(compute(3)) #3878983057768
    print(compute(103)) #492700616748525
    print(compute(1000003))
    print("--- %s seconds ---" % (time.time() - start_time))