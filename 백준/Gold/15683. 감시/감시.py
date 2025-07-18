import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
obs = 0
cctv = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 6:
            obs += 1
        elif line[j] != 0:
            cctv.append((line[j], (i, j)))
    board.append(line)

len_cctv = len(cctv)
zeros = N * M - len_cctv - obs
sharps = 0
unbld_set = set()
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def func(w):
    global sharps
    if w == len_cctv:
        sharps = max(sharps, len(unbld_set))
        return
        
    c = cctv[w]
    if c[0] == 1:
        cctv_1(w, c[1])
    if c[0] == 2:
        cctv_2(w, c[1])
    if c[0] == 3:
        cctv_3(w, c[1])
    if c[0] == 4:
        cctv_4(w, c[1])
    if c[0] == 5:
        cctv_5(w, c[1])

def watch(xx, yy, dir_n):
    return_list = []
    while True:
        xx += dx[dir_n]
        yy += dy[dir_n]
        if not (0 <= xx < N and 0 <= yy < M and board[xx][yy] != 6):
            break

        if board[xx][yy] == 0 and (xx, yy) not in unbld_set:
            return_list.append((xx, yy))

    return return_list

def cctv_1(w, t):
    global unbld_set 
    for n in range(4):
        xx, yy = t
        watched = watch(xx, yy, n)
        watched_set = set(watched)
        unbld_set.update(watched_set)
        func(w+1)
        unbld_set -= watched_set

def cctv_2(w, t):
    global unbld_set 
    for n in range(2):
        xx, yy = t
        watched_1 = watch(xx, yy, n)
        watched_2 = watch(xx, yy, n+2)
        watched_set = set(watched_1 + watched_2)
        unbld_set.update(watched_set)
        func(w+1)
        unbld_set -= watched_set

def cctv_3(w, t):
    global unbld_set 
    for n in range(4):
        xx, yy = t
        watched_1 = watch(xx, yy, n)
        watched_2 = watch(xx, yy, (n+1)%4)
        watched_set = set(watched_1 + watched_2)
        unbld_set.update(watched_set)
        func(w+1)
        unbld_set -= watched_set

def cctv_4(w, t):
    global unbld_set 
    for n in range(4):
        xx, yy = t
        watched_1 = watch(xx, yy, (n-1)%4)
        watched_2 = watch(xx, yy, n)
        watched_3 = watch(xx, yy, (n+1)%4)
        watched_set = set(watched_1 + watched_2 + watched_3)
        unbld_set.update(watched_set)
        func(w+1)
        unbld_set -= watched_set

def cctv_5(w, t):
    global unbld_set 
    xx, yy = t
    watched_1 = watch(xx, yy, 0)
    watched_2 = watch(xx, yy, 1)
    watched_3 = watch(xx, yy, 2)
    watched_4 = watch(xx, yy, 3)
    watched_set = set(watched_1 + watched_2 + watched_3 + watched_4)
    unbld_set.update(watched_set)
    func(w+1)
    unbld_set -= watched_set

func(0)
print(zeros - sharps)