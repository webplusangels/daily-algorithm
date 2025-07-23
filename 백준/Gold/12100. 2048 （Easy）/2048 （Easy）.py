import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
bd = []
for _ in range(N):
    line = list(map(int, input().split()))
    bd.append(line)

def up(board):
    cache = [board[i][:] for i in range(N)]
    for j in range(N):
        l = [board[i][j] for i in range(N) if board[i][j] != 0]
        new_l = deque()
        saved = 0
        for num in l:
            if saved:
                if saved == num:
                    new_l.append(saved * 2)
                    saved = 0
                else:
                    new_l.append(saved)
                    saved = num
            else:
                saved = num
        if saved:
            new_l.append(saved)
            
        if new_l:
            for i in range(N):
                num = 0
                if new_l:
                    num = new_l.popleft()
                cache[i][j] = num
    return cache

def down(board):
    cache = [board[i][:] for i in range(N)]
    for j in range(N):
        l = [board[i][j] for i in range(N) if board[i][j] != 0]
        new_l = deque()
        saved = n = 0
        for _ in range(len(l)):
            n -= 1
            num = l[n]
            if saved:
                if saved == num:
                    new_l.append(saved * 2)
                    saved = 0
                else:
                    new_l.append(saved)
                    saved = num
            else:
                saved = num     
        if saved:
            new_l.append(saved)

        if new_l:
            for i in range(1, N+1):
                num = 0
                if new_l:
                    num = new_l.popleft()
                cache[-i][j] = num
    return cache

def left(board):
    cache = [board[i][:] for i in range(N)]
    for i in range(N):
        l = [board[i][j] for j in range(N) if board[i][j] != 0]
        new_l = deque()
        saved = 0
        for num in l:
            if saved:
                if saved == num:
                    new_l.append(saved * 2)
                    saved = 0
                else:
                    new_l.append(saved)
                    saved = num
            else:
                saved = num     
        if saved:
            new_l.append(saved)
            
        if new_l:
            for j in range(N):
                num = 0
                if new_l:
                    num = new_l.popleft()
                cache[i][j] = num
    return cache


def right(board):
    cache = [board[i][:] for i in range(N)]
    for i in range(N):
        l = [board[i][j] for j in range(N) if board[i][j] != 0]
        new_l = deque()
        saved = n = 0
        for _ in range(len(l)):
            n -= 1
            num = l[n]
            if saved:
                if saved == num:
                    new_l.append(saved * 2)
                    saved = 0
                else:
                    new_l.append(saved)
                    saved = num
            else:
                saved = num     
        if saved:
            new_l.append(saved)

        if new_l:
            for j in range(1, N+1):
                num = 0
                if new_l:
                    num = new_l.popleft()
                cache[i][-j] = num
    return cache

def to_the_max(m, cache):
    for i in range(N):
        for j in range(N):
            if cache[i][j] > m:
                m = cache[i][j]
    return m
    
mm = 0
# 최대 5번
def func(w, b):
    global mm
    if w == 5:
        mm = to_the_max(mm, b)
        return

    for n in range(4):
        if n == 0:
            cache = up(b)
        elif n == 1:
            cache = down(b)
        elif n == 2:
            cache = right(b)
        elif n == 3:
            cache = left(b)
        func(w+1, cache)

func(0, bd)
print(mm)