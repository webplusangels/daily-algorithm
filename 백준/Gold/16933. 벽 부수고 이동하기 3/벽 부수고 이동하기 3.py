import sys
from collections import deque

N, M, K = map(int, input().split())
area = []

for _ in range(N):
    line = list(map(int, list(input())))
    area.append(line)

vis = [[[False] * (K+1) for _ in range(M)] for _ in range(N)]
dq = deque()

dq.append((0, 0, K, 1))
vis[0][0][K] = True

day = True
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

while dq:
    flag = False
    x, y, k, cnt = dq.popleft()
    if x == N-1 and y == M-1:
        print(cnt)
        break
    for n in range(4):
        xx, yy = dx[n] + x, dy[n] + y
        if 0 <= xx < N and 0 <= yy < M:
            if area[xx][yy] == 0 and not vis[xx][yy][k]:
                dq.append((xx, yy, k, cnt+1))
                vis[xx][yy][k] = True
            if k and area[xx][yy] == 1 and not vis[xx][yy][k-1]:
                if cnt % 2:
                    dq.append((xx, yy, k-1, cnt+1))
                    vis[xx][yy][k-1] = True
                else:
                    flag = True
    # night일 때 벽을 부셔야 한다면
    if flag:
        dq.append((x, y, k, cnt+1))

else:
    print(-1)