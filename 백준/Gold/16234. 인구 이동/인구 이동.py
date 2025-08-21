import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def func():
    dq = deque()
    union = []
    capacity = []
    vis = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if vis[i][j] == True:
                continue
            dq.append((i, j))
            tmp_u = [(i, j)]
            tmp_c = [A[i][j]]
            vis[i][j] = True
            while dq:
                x, y = dq.popleft()
                for n in range(4):
                    xx, yy = x+dx[n], y+dy[n]
                    if 0 <= xx < N and 0 <= yy < N and not vis[xx][yy] and L <= abs(A[xx][yy]-A[x][y]) <= R:
                        dq.append((xx, yy))
                        tmp_u.append((xx, yy))
                        tmp_c.append(A[xx][yy])
                        vis[xx][yy] = True
            union.append(tmp_u)
            capacity.append(tmp_c)
    return union, capacity

while True:
    union, cap = func()
    # print(f"{union=}, {cap=}")
    l = len(union)
    if l == N*N:
        print(cnt)
        break
    for i in range(l):
        new_cap = sum(cap[i]) // len(cap[i])
        for (x, y) in union[i]:
            A[x][y] = new_cap
    cnt += 1
    # print(A)