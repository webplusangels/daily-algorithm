from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
maze_map = []

for _ in range(N):
    num = input()
    maze_map.append([int(n) for n in num])

cnt_map = [[0 for _ in range(M)] for _ in range(N)]
dq = deque([(0, 0)])
maze_map[0][0] = 0
cnt_map[0][0] = 1

while dq:
    i, j = dq.popleft()
    if i+1 < N and maze_map[i+1][j]:
        dq.append((i+1, j))
        maze_map[i+1][j] = 0
        cnt_map[i+1][j] = 1 + cnt_map[i][j]
    if j+1 < M and maze_map[i][j+1]:
        dq.append((i, j+1))
        maze_map[i][j+1] = 0
        cnt_map[i][j+1] = 1 + cnt_map[i][j]
    if i-1 >= 0 and maze_map[i-1][j]:
        dq.append((i-1, j))
        maze_map[i-1][j] = 0
        cnt_map[i-1][j] = 1 + cnt_map[i][j]
    if j-1 >= 0 and maze_map[i][j-1]:
        dq.append((i, j-1))
        maze_map[i][j-1] = 0
        cnt_map[i][j-1] = 1 + cnt_map[i][j]

print(cnt_map[N-1][M-1])