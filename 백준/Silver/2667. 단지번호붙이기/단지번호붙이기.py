from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N = int(input())
square = []

for _ in range(N):
    line = list(map(int, list(input())))
    square.append(line)

dq = deque()
vis = [[True for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
c_list = []

for i in range(N):
    for j in range(N):
        if square[i][j] == 1 and vis[i][j]:
            vis[i][j] = False
            dq.append((i, j))
            count = 1
            while dq:
                x, y = dq.popleft()
                for n in range(4):
                    xx = dx[n] + x
                    yy = dy[n] + y
                    if 0 <= xx < N and 0 <= yy < N and square[xx][yy] == 1 and vis[xx][yy]:
                        vis[xx][yy] = False
                        dq.append((xx, yy))
                        count += 1
            c_list.append(count)

print(len(c_list))
for c in sorted(c_list):
    print(c)