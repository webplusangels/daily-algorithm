import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

sum_board = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        n = sum_board[i][j-1] + sum_board[i-1][j] - sum_board[i-1][j-1]
        sum_board[i][j] = n + board[i-1][j-1]

# ========== 출력 ==============
# for i in range(len(board)):
#     print(*board[i])

# for i in range(len(sum_board)):
#     print(*sum_board[i])

# ==============================

def check(x1, y1, x2, y2):
    if x1 < 1 or y1 < 1 or x2 > N or y2 > M:
        return False
    # print(f"{x1=}, {x2=}, {y1=}, {y2=}")
    c = sum_board[x2][y2] - sum_board[x1-1][y2] - sum_board[x2][y1-1] + sum_board[x1-1][y1-1]
    if c:
        return False
    else:
        return True
    
dq = deque([(Sr, Sc, 0)])
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
iter = 0
vis = set([(Sr, Sc)])
while dq:
    x, y, iter = dq.popleft()
    if x == Fr and y == Fc:
        print(iter)
        break
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        nxx, nyy = nx+H-1, ny+W-1
        if (nx, ny) not in vis and check(nx, ny, nxx, nyy):
            dq.append((nx, ny, iter+1))
            vis.add((nx, ny))
else:
    print(-1)