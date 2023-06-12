# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:41:29 2023

@author: igorvanloo
"""
'''
Project Euler Problem 313

Problem should have some sort of recursive structure because with optimal moves we can make the board into 
a smaller board

Using class SlidingGame the following patterns emerge

S(2, 2) = 5
S(2, 3) = 9 (+4)
S(2, 4) = 15 (+6)
S(2, 5) = 21 (+6)
S(2, 6) = 27 (+6)

S(3, 3) = 13
S(3, 4) = 17 (+4)
S(3, 5) = 23 (+6)
S(3, 6) = 29 (+6)
S(3, 7) = 35 (+6)
S(3, 8) = 41 (+6)

S(4, 4) = 21
S(4, 5) = 25 (+4)
S(4, 6) = 31 (+6)
S(4, 7) = 37 (+6)

S(5, 5) = 29
S(5, 6) = 33 (+4)
S(5, 7) = 39 (+6)

We can see that 
1. S(n, n) = 8 + S(n - 1, n - 1), S(2, 2) = 5
2. S(m, n + 1) = 6 + S(m, n) if n > m + 1
               = 4 + S(m, n) if n = m + 1
               
We can combine these S(m, n) = 4*(n - m) + 2*(n - m - 1) + S(m, m)
                             = 4*(n - m) + 2(n - m - 1) + 8*(m - 2) + 5
                             
Therefore we have S(m, n) = 8*m - 11         if m = n
                          = 6*n + 2*m - 13   if n > m

p^2 = 6n + 2m - 13
x = (p^2 + 13)/2 = 3n + m

since n >= m, 4n >= 3n + m = x and 4m <= 3n + m = x
=> m <= x/4
=> n >= x/4 

Anwser:
    2057774861813004
--- 0.17411136627197266 seconds ---
'''
import time, math
start_time = time.time()

class SlidingGame:
    
    def __init__(self, m, n):
        self.board = self.create_board(m, n)
        self.solution = self.find_best_path(self.board, m, n)
    
    def create_board(self, m, n):
        board = []
        for x in range(n):
            board.append([1]*m)
        board[0][0] = 2
        board[-1][-1] = 0
        return board
    
    def move_piece(self, board, x, y, d):
        v = board[x][y]
        if d == "n":
            new_x, new_y = x - 1, y
        if d == "s":
            new_x, new_y = x + 1, y
        if d == "e":
            new_x, new_y = x, y + 1
        if d == "w":
            new_x, new_y = x, y - 1
            
        board[new_x][new_y] = v
        board[x][y] = 0
        return board
    
    def find_movable_pieces(self, board, empty_x, empty_y, m, n):
        pieces = []
        if empty_x + 1 < n:
            pieces.append((empty_x + 1, empty_y, "n"))
        
        if empty_x - 1 >= 0:
            pieces.append((empty_x - 1, empty_y, "s"))
        
        if empty_y + 1 < m:
            pieces.append((empty_x, empty_y + 1, "w"))
        
        if empty_y - 1 >= 0:
            pieces.append((empty_x, empty_y - 1, "e"))
        
        return pieces
    
    def create_board_id(self, board, m, n):
        board_id = ""
        for x in range(n):
            for y in range(m):
                board_id += str(board[x][y])
        return board_id
    
    def print_board(self, board, n):
        for x in range(n):
            print(board[x])
    
    def copy_board(self, board, m, n):
        new_board = []
        for x in range(n):
            t = []
            for y in range(m):
                t.append(board[x][y])
            new_board.append(t)
        return new_board
    
    def print_path(self, path, n):
        for i, x in enumerate(path):
            print(i)
            self.print_board(x, n)
            
    def find_best_path(self, board, m, n):
        
        queue = [(board, n - 1, m - 1, 0, (board,))]
        seen = []
        while queue != []:
            b, empty_x, empty_y, move, path = queue.pop(0)
            board_id = self.create_board_id(b, m, n)
            
            if board_id not in seen:
                seen.append(board_id)
                for xx, yy, d in self.find_movable_pieces(b, empty_x, empty_y, m, n):
                    temp_board = self.copy_board(b, m, n)
                    new_board = self.move_piece(temp_board, xx, yy, d)
                    new_path = path + (new_board, )
                    if new_board[-1][-1] == 2:
                        return move + 1
                    queue.append((new_board, xx, yy, move + 1, new_path))
            
def S_brute_force(m, n):
    s = SlidingGame(m, n)
    return s.solution

def compute_brute_force(limit):
    primes = list_primes(limit)
    res = {p*p:0 for p in primes}
    maxi = primes[-1]*primes[-1]
    
    m = 2
    while True:
        print(m)
        if S(m, m) > maxi:
            break
        
        n = m
        while True:
            t = S(m, n)
            if t > maxi:
                break
            if t in res:
                res[t] += 1
            n += 1
        m += 1
    #print([p*p/res[p*p] for p in primes[1:]])
    return 2*sum(res[p*p] for p in primes)

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

def S(m, n):
    if m == n:
        #8*(m - 2) + 5
        #8m - 11
        return 8*m - 11
    #4*(n - m) + 2*(n - m - 1) + 8*(m - 2) + 5
    #4n - 4m + 2n - 2m - 2 + 8m - 16 + 5
    #6n + 2m - 13
    return 6*n + 2*m - 13

def compute(limit):
    primes = list_primes(limit)
    total = 1
    for p in primes[2:]:
        #(p*p - 13)/2 = 3n + m
        #x = 3n + m >= 4m since n >= m
        #m =< x//4
        #So for all m <= x//4 we test if (x - m) % 3 == 0
        #This is the same as finding the number of integers between x - x//4 and x which are divisble by 3
        #which is the same as finding number of integres between 0 and x//4 divisble by 3
        #which is the same as x//12 + 1
        total += ((p*p - 13)//8 - 1)//3 + 1
    return 2*total

if __name__ == "__main__":
    print(compute(10**6))
    print("--- %s seconds ---" % (time.time() - start_time))
