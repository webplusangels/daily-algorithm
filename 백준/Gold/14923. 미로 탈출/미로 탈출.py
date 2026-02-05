import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
Hx, Hy = map(lambda x: int(x) - 1, input().split())
Ex, Ey = map(lambda x: int(x) - 1, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

# 0이 빈 칸, 1이 벽, 한 번의 벽을 부술 수 있는 기회
vis = [[[False]*2 for _ in range(M)] for _ in range(N)]
vis[Hx][Hy][1] = True
dq = deque([(Hx, Hy, 1, 0)]) # x, y, 기회, 이동 횟수

while dq:
    x, y, op, move = dq.popleft()
    if x == Ex and y == Ey:
        print(move)
        break
    
    for n in range(4):
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < N and 0 <= ny < M:
            if not vis[nx][ny][op] and board[nx][ny] == 0:
                dq.append((nx, ny, op, move+1))
                vis[nx][ny][op] = True
            elif op == 1 and not vis[nx][ny][op-1] and board[nx][ny] == 1:
                dq.append((nx, ny, op-1, move+1))
                vis[nx][ny][op-1] = True
else:
    print(-1)