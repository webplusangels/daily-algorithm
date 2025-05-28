from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N = int(input())
pic = []

for _ in range(N):
    line = input()
    pic.append(list(line))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 적록용
pic_ts = [['R' if color != 'B' else 'B' for color in line] for line in pic]

def bfs(pic):
    N = len(pic)
    cnt = 0
    dq = deque()
    for i in range(N):
        for j in range(N):
            if pic[i][j] != 'X':
                dq.append((i, j))
                cnt += 1
            while dq:
                x, y = dq.popleft()
                color = pic[x][y]
                pic[x][y] = 'X'
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0 <= xx < N and 0 <= yy < N and color == pic[xx][yy] and pic[xx][yy] != 'X':
                        dq.append((xx, yy))
    return cnt

print(f"{bfs(pic)} {bfs(pic_ts)}")