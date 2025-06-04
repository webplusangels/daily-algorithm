from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
vis = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
area = []

for _ in range(N):
    line = list(map(int, list(input())))
    area.append(line)

dq = deque([(0, 0, 1, 0)])
vis[0][0][1] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while dq:
    x, y, brk, cnt = dq.popleft()
    if (x, y) == (N-1, M-1):
        print(cnt+1)
        break
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if 0 <= xx < N and 0 <= yy < M and not vis[xx][yy][brk]:
            if area[xx][yy] == 0:
                vis[xx][yy][brk] = True
                dq.append((xx, yy, brk, cnt+1))
            if area[xx][yy] == 1 and brk:
                vis[xx][yy][brk] = True
                dq.append((xx, yy, brk-1, cnt+1))
else:
    print(-1)