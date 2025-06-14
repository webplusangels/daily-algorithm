import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
area = []
dqs = [deque() for _ in range(P+1)]
cnt = [0 for _ in range(P+1)]
vis = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    line = list(input())
    for j in range(M):
        char = line[j]
        if char != '#' and char != '.':
            line[j] = int(char)
            dqs[line[j]].append((i, j))
            cnt[line[j]] += 1
            vis[i][j] = line[j]
    area.append(line)

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
flag = True

while flag:
    flag = False
    for i in range(1, P+1):
        for _ in range(S[i]):
            if not dqs[i]:
                break
            for _ in range(len(dqs[i])):
                x, y = dqs[i].popleft()
                for n in range(4):
                    xx, yy = dx[n] + x, dy[n] + y
                    if 0 <= xx < N and 0 <= yy < M and not vis[xx][yy] and area[xx][yy] == '.':
                        dqs[i].append((xx, yy))
                        vis[xx][yy] = vis[x][y]
                        cnt[i] += 1
                        flag = True

print(*cnt[1:])
