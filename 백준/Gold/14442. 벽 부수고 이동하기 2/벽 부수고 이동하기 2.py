import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
area = []
for _ in range(N):
    line = list(map(int, list(input())))
    area.append(line)

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
vis = [[[False for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]

vis[0][0][K] = True
dq = deque([(0, 0, K, 1)])

while dq:
    x, y, k, cnt = dq.popleft()
    if x == N - 1 and y == M - 1:
        print(cnt)
        break
    for n in range(4):
        xx, yy = dx[n] + x, dy[n] + y
        if 0 <= xx < N and 0 <= yy < M:
            if area[xx][yy] == 1 and k > 0 and not vis[xx][yy][k-1] :
                dq.append((xx, yy, k-1, cnt+1))
                vis[xx][yy][k-1] = True
            elif area[xx][yy] == 0 and not vis[xx][yy][k]:
                dq.append((xx, yy, k, cnt+1))
                vis[xx][yy][k] = True
else:
    print(-1)