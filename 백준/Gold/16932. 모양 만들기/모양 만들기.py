import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [[int(n) for n in input().split()] for _ in range(N)]

s_board = [[0]*M for _ in range(N)]
vis = [[0]*M for _ in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

zeros = set()
marker = 1

for i in range(N):
    for j in range(M):
        if vis[i][j]: continue
        if board[i][j] == 0: 
            vis[i][j] = -1
            zeros.add((i, j))
            continue

        dq = deque([(i, j)])
        vis[i][j] = marker
        coors = [(i, j)]
        while dq:
            x, y = dq.popleft()

            for n in range(4):
                nx, ny = x+dx[n], y+dy[n]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and not vis[nx][ny]:
                    dq.append((nx, ny))
                    coors.append((nx, ny))
                    vis[nx][ny] = marker

        size = len(coors)
        for c in coors:
            x, y = c
            s_board[x][y] = size
        else:
            marker += 1

mx = 0


for z in zeros:
    x, y = z
    ter = set()
    size = 1
    
    for n in range(4):
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < N and 0 <= ny < M and vis[nx][ny] > 0 and vis[nx][ny] not in ter:
            size += s_board[nx][ny]
            ter.add(vis[nx][ny])

    mx = max(size, mx)

print(mx)