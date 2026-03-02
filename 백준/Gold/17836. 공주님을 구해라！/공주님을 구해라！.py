import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 2차원 + 검이 있는지 없는지
N, M, T = map(int, input().split())
board = [[int(n) for n in input().split()] for _ in range(N)]

vis = [[[False]*2 for _ in range(M)] for _ in range(N)]

# x, y, sword, moves
dq = deque([(0, 0, 0, 0)])
vis[0][0][0] = True

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

while dq:
    x, y, sword, moves = dq.popleft()

    if moves > T:
        continue

    if x == N-1 and y == M-1:
        print(moves)
        break

    for n in range(4):
        nx, ny = x+dx[n], y+dy[n]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 2:
                sword_n = 1
            else:
                sword_n = sword
            if vis[nx][ny][sword_n]:
                continue
            if board[nx][ny] == 1 and not sword_n:
                continue
            
            dq.append((nx, ny, sword_n, moves+1))
            vis[nx][ny][sword_n] = True

else:
    print('Fail')