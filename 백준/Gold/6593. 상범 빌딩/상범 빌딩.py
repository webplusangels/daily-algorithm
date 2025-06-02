from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

def bfs(L, R, C, cube, S, E):
    vis = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    dq = deque()
    dq.append(S)
    vis[S[0]][S[1]][S[2]] = 0
    
    while dq:
        i, j, k = dq.popleft()
        if (i, j, k) == E:
            print(f"Escaped in {vis[i][j][k]} minute(s).")
            return
        for n in range(6):
            xx = dx[n] + i
            yy = dy[n] + j
            zz = dz[n] + k
            if 0 <= xx < L and 0 <= yy < R and 0 <= zz < C and \
                cube[xx][yy][zz] != "#" and vis[xx][yy][zz] == -1:
                dq.append((xx, yy, zz))
                vis[xx][yy][zz] = vis[i][j][k] + 1

    print("Trapped!")

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    cube = []
    S = E = None
    for l in range(L):
        area = []
        for r in range(R):
            line = list(input())
            for i, c in enumerate(line):
                if c == 'S':
                    S = (l, r, i)
                if c == 'E':
                    E = (l, r, i)
            area.append(line)
        input()
        cube.append(area)

    bfs(L, R, C, cube, S, E)