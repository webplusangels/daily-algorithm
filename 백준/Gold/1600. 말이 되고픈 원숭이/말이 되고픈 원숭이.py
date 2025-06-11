from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

# 입력
K = int(input())
W, H = map(int, input().split())
area = []

for _ in range(H):
    line = list(map(int, input().split()))
    area.append(line)

# 방문 배열 (원숭이의 남은 동작 수 * W * H)
vis = [[[False for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

# x, y, k, cnt를 deque에 추가해 초기화
dq = deque([(0, 0, K, 0)])
vis[0][0][K] = True

# 좌표 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
hx, hy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]

while dq:
    x, y, k, cnt = dq.popleft()
    if x == H - 1 and y == W - 1:
        print(cnt)
        break
    
    for n in range(4):
        xx, yy = dx[n] + x, dy[n] + y
        if 0 <= xx < H and 0 <= yy < W and not area[xx][yy] and not vis[xx][yy][k]:
            dq.append((xx, yy, k, cnt + 1))
            vis[xx][yy][k] = True

    if k != 0:
        for n in range(8):
            xx, yy, kk = hx[n] + x, hy[n] + y, k-1
            if 0 <= xx < H and 0 <= yy < W and not area[xx][yy] and not vis[xx][yy][kk]:
                dq.append((xx, yy, kk, cnt + 1))
                vis[xx][yy][kk] = True
else:
    print(-1)