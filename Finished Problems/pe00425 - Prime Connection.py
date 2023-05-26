# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:48:13 2023

@author: igorvanloo
"""
'''
Project Euler Problem 425

Create a graph where there is an edge between each now p, q if p, q are directly connected

for example 2 is directly connected to 3, 5, 7, 23, 29, and the weight of this edge is the larger prime

for example edge between 2 and 29 has weight 29

Now if we compute the Widest Path Problem: https://en.wikipedia.org/wiki/Widest_path_problem
Then we can find a path from 2 to every prime such that the the maximal element of the path is minimized

I used my previously built Dijkstras and https://stackoverflow.com/questions/18552964/finding-path-with-maximum-minimum-capacity-in-graph/18553217#18553217
to create a modified Dijkstras algorithm to solve this and it worked! However it is still too slow to actually
create the graph :/ takes about a ~80 sec to solve F(10**5)

Fixed creation of graph a bit, gets F(10**5) in ~15 sec

Made the dijkstras algorithm more efficient get F(10**5) in ~5 sec, F(10**6) in ~372 sec

Switched from lists to dictionarys, huge speed up

Switched from slow priority queue to fast priority queue and can finally solve the problem!

Anwser:
    46479497324
--- 36.6098096370697 seconds ---
'''
import time, math, heapq
start_time = time.time()

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

def add_to_heap(heap, element):
    heap.append(element)
    index = len(heap) - 1
    parent_index = math.ceil(index/2) - 1
    parent = heap[parent_index]
    
    while (parent_index > -1 and parent[0] > element[0]):
        heap[parent_index] = element
        heap[index] = parent
        
        index = parent_index
        parent_index = math.ceil(index/2) - 1
        parent = heap[parent_index]
    
    return heap            
    
def remove_min_from_heap(heap):
    parent = heap.pop(-1)
    #If our list is empty after removing we return empty list
    if len(heap) == 0:
        return []
    #If our list has one element left, the removed element becomes the head and we return it
    if len(heap) == 1:
        heap[0] = parent
        return heap
    if len(heap) == 2:
        heap[0] = parent
        if heap[0] > heap[1]:
            return heap[::-1]
        return heap
    
    heap[0] = parent
    
    parent_index = 0
    child_left_index = 1
    child_right_index = 2
    
    parent = heap[parent_index]
    
    if heap[child_left_index] > heap[child_right_index]:
        child_index = child_right_index
    else:
        child_index = child_left_index
        
    child = heap[child_index]
    
    while parent > child:
        #We swap the parent and the child
        heap[child_index] = parent
        heap[parent_index] = child
        
        #Update the index's
        parent_index = child_index
        child_left_index = 2*parent_index + 1
        child_right_index = child_left_index + 1
        
        #Make sure we dont encounter an index error
        #If your right child is less than length of heap then we compare left and right child
        if child_right_index < len(heap):
            if heap[child_left_index] > heap[child_right_index]:
                child_index = child_right_index
            else:
                child_index = child_left_index
                
            parent = heap[parent_index]
            child = heap[child_index]
        #Our right child is more, if our left child is less than length of heap then it is the 
        #Only available one
        elif child_left_index < len(heap):
            child_index = child_left_index
            
            parent = heap[parent_index]
            child = heap[child_index]
        #No children left, we break the while loop
        else:
            break
                
    return heap

def widest(graph, start = 0, INFINITY = 10**10):
    #https://en.wikipedia.org/wiki/Widest_path_problem
    #https://stackoverflow.com/questions/18552964/finding-path-with-maximum-minimum-capacity-in-graph/18553217#18553217
    width = {}
    cloud = {}
    path = {}
    for x in graph:
        width[x] = INFINITY
        cloud[x] = False
        #path[x] = (2,)
        
    width[start] = 0
    queue = [(2, 2)]
    while len(queue) != 0:
        
        wu, u = queue[0]
        remove_min_from_heap(queue)
        
        cloud[u] = True
        
        if wu == INFINITY:
            break
        
        for v, w in graph[u]:
            if cloud[v] == False:
                alt = min(width[v], max(wu, w))
                if alt < width[v]:
                    #path[v] = path[u] + (v,)
                    width[v] = alt
                    add_to_heap(queue, (width[v], v))
        
    return width, path

def F(N):
    is_prime = list_primality(N)
    primes = [i for (i, isprime) in enumerate(is_prime) if isprime]
    graph = {}
                    
    for k in range(len(primes)):
        p = primes[k]
        
        digits = []
        while p != 0:
            digits.append(p % 10)
            p //= 10
        digits.append(0)
        digits = digits[::-1]
        
        p = primes[k]
        for x in range(len(digits)):
            og = digits[x]
            for i in range(og + 1, 10):
                digits[x] = i  
                num = 0
                for y in digits:
                    num = 10*num + y
                
                if num <= primes[-1] and num != p:
                    if is_prime[num]:
                        if p in graph:
                            graph[p].append((num, num))
                        else:
                            graph[p] = [(num, num)]
                            
                        if num in graph:
                            graph[num].append((p, num))
                        else:
                            graph[num] = [(p, num)]
            digits[x] = og
    
    D, path = widest(graph, 2)
    res = 0
    for p in primes:
        if p in D:
            if D[p] > p:
                res += p
        else:
            res += p
    return res

if __name__ == "__main__":
    print(F(10**7))
    print("--- %s seconds ---" % (time.time() - start_time))
