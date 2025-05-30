from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

M, N, K = map(int, input().split())
rec = [[True for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            rec[i][j] = False

dq = deque()
cnt = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(M):
    for j in range(N):
        if rec[i][j]:
            rec[i][j] = False
            dq.append((i, j))
            area = 0
            while dq:
                x, y = dq.popleft()
                area += 1
                for num in range(4):
                    xx = dx[num] + x
                    yy = dy[num] + y
                    if 0 <= xx < M and 0 <= yy < N and rec[xx][yy]:
                        rec[xx][yy] = False
                        dq.append((xx, yy))
            cnt.append(area)
            
print(len(cnt))
print(*sorted(cnt))