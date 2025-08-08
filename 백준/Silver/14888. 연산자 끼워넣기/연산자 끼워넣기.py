import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
As = deque([int(e) for e in input().split()])
ops = [int(e) for e in input().split()]

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def prod(a, b):
    return a * b
def div(a, b):
    if a < 0:
        return -(-a // b)
    return a // b
    
def operator(n, a, b):
    if n == 0:
        return add(a, b)
    elif n == 1:
        return sub(a, b)
    elif n == 2:
        return prod(a, b)
    elif n == 3:
        return div(a, b)

MIN = float('inf')
MAX = float('-inf')
def func(w, cnt):
    global MIN
    global MAX
    
    if w == N:
        MIN = min(MIN, cnt)
        MAX = max(MAX, cnt)
        return

    for j in range(4):
        if ops[j]:
            ops[j] -= 1
            n_cnt = operator(j, cnt, As[w])
            func(w+1, n_cnt)
            ops[j] += 1
            
func(1, As[0])

print(MAX)
print(MIN)
