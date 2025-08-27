import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
virus = []
lab = []
av = N*N
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            virus.append((i, j))
            av -= 1
        if line[j] == 1:
            av -= 1
    lab.append(line)

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(w):
    if av == 0:
        return 0
    dq = deque(w)
    mm = virused = 0
    vis = [[-1]*N for _ in range(N)]
    for x, y in w:
        vis[x][y] = 0

    while dq:
        x, y = dq.popleft()
        cnt = vis[x][y]
        for n in range(4):
            xx, yy = x+dx[n], y+dy[n]
            if 0 <= xx < N and 0 <= yy < N and vis[xx][yy] == -1:
                if lab[xx][yy] == 2:
                    if virused == av:
                        continue
                    vis[xx][yy] = cnt+1
                    dq.append((xx, yy))
                elif lab[xx][yy] != 1:
                    vis[xx][yy] = cnt+1
                    dq.append((xx, yy))
                    virused += 1
                    mm = max(mm, cnt+1)

    # print(*vis, sep='\n')
    # print()
    if virused == av:
        # print(mm)
        return mm
    else:
        # print(-1)
        return -1

num_virus = len(virus)
answer = float('inf')
def func(w, n):
    global answer
    if len(w) == M:
        a = bfs(w)
        if a >= 0:
            answer = min(answer, a)

    for i in range(n, num_virus):
        w.append(virus[i])
        func(w, i+1)
        w.pop()

func([], 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)