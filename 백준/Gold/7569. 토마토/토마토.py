from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

M, N, H = map(int, input().split())
tomatoes = []

for _ in range(H):
    tmp = []
    for _ in range(N):
        nums = list(map(int, input().split()))
        tmp.append(nums)
    tomatoes.append(tmp)

tom_dq = deque()
vis = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
m = -1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                tom_dq.append((i, j, k, 0))
                vis[i][j][k] = 1
            if tomatoes[i][j][k] == -1:
                vis[i][j][k] = 1
   
while tom_dq:
    x, y, z, cnt = tom_dq.popleft()
    m = max(m, cnt)
    for i in range(6):
        xx = dx[i] + x
        yy = dy[i] + y
        zz = dz[i] + z

        if 0 <= xx < H and 0 <= yy < N and 0 <= zz < M and \
            tomatoes[xx][yy][zz] == 0 and vis[xx][yy][zz] != 1:
            tom_dq.append((xx, yy, zz, cnt+1))
            vis[xx][yy][zz] = 1

# 다 안 익었을 때
def find_zero(matrix):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if vis[i][j][k] == 0:
                    return True
    return False

if find_zero(vis):
    print(-1)
else:
    if m == -1:
        print(0)
    else:
        print(m)