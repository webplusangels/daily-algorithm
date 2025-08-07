import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
get_ints = lambda: map(int, input().split())

N, M = get_ints()
virus = []
board = []
for i in range(N):
    line = list(get_ints())
    for j in range(M):
        if line[j] == 2:
            virus.append((i, j))
    board.append(line)

m = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(l):
    bd = [board[i][:] for i in range(N)]
    for coor in l:    
        bd[coor[0]][coor[1]] = 1

    dq = deque(virus)
    while dq:
        x, y = dq.popleft()
        for nn in range(4):
            xx, yy = x+dx[nn], y+dy[nn]
            if 0 <= xx < N and 0 <= yy < M and bd[xx][yy] == 0:
                bd[xx][yy] = 2
                dq.append((xx, yy))

    answer = 0
    for i in range(N):
        answer += bd[i].count(0)
    return answer

w = []
def func(n):
    global m
    if len(w) == 3:
        num = bfs(w)
        m = max(num, m)
        return

    for rep in range(n, N*M):
        i, j = rep//M, rep%M
        if board[i][j] == 0:
            w.append((i, j))
            func(rep+1)
            w.pop()

func(0)
print(m)