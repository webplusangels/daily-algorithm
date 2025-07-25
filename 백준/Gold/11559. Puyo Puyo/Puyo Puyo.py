import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

board = []
for _ in range(12):
    line = list(input())
    board.append(line)

start = None
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
cnt = 0

def bfs(x, y, vis):
    dq = deque([(x, y)])
    string = board[x][y]
    ys = [(x, y)]
    while dq:
        xi, yi = dq.popleft()
        for n in range(4):
            xx, yy = xi + dx[n], yi + dy[n]
            if 0 <= xx < 12 and 0 <= yy < 6 and board[xx][yy] == string and not vis[xx][yy]:
                ys.append((xx, yy))
                dq.append((xx, yy))
                vis[xx][yy] = True
    return ys, vis

def gravity():
    global cnt
    for j in range(6):
        y_list = [board[i][j] for i in range(12) if board[i][j] != '.']
        for i in range(1, 13):
            char = '.'
            if y_list:
                char = y_list.pop()
            board[-i][j] = char
    cnt += 1

while True:
    visited = [[False]*6 for _ in range(12)]
    flag = True
    for i in range(12):
        for j in range(6):
            if board[i][j].isalpha() and not visited[i][j]:
                visited[i][j] = True
                ys, visited = bfs(i, j, visited)
                if len(ys) >= 4:
                    flag = False
                    for (x, y) in ys:
                        board[x][y] = '.'
            else:
                visited[i][j] = True
    if flag:
        break
    
    gravity()

print(cnt)