import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

squares = []
for i in range(5):
    square = []
    for j in range(5):
        line = list(map(int, input().split()))
        square.append(line)
    squares.append(square)

def rotate(square):
    rotated = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            x, y = j, 4-i
            rotated[x][y] = square[i][j]
    return rotated

def rotate_four(sqaure):
    square_1 = rotate(square)
    square_2 = rotate(square_1)
    square_3 = rotate(square_2)

    return square, square_1, square_2, square_3

r_sqrs = []
for square in squares:
    rtd = rotate_four(square)
    r_sqrs.append(rtd)

dx, dy, dz = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)
m = float('inf')
def bfs(maze):
    global m
    dq, cnt = deque([(0, 0, 0)]), 0
    visited = set()
    while dq:
        for _ in range(len(dq)):
            x, y, z = dq.popleft()
            if (x, y, z) == (4, 4, 4):
                return cnt
            for n in range(6):
                xx, yy, zz = x+dx[n], y+dy[n], z+dz[n]
                if 0 <= xx < 5 and 0 <= yy < 5 and 0 <= zz < 5 and \
                    (xx, yy, zz) not in visited and maze[zz][xx][yy]:
                    visited.add((xx, yy, zz))
                    dq.append((xx, yy, zz))
        cnt += 1
        if cnt >= m:
            break
    return -1
        
vis = [False] * 5
def func(maze):
    global m
    if all(vis):
        r = bfs(maze)
        if r != -1:
            m = min(m, r)

    for i in range(5):
        if vis[i]:
            continue
        else:
            vis[i] = True
            for n in range(4):
                if len(maze) == 0 and not r_sqrs[i][n][0][0]:
                    continue
                if len(maze) == 4 and not r_sqrs[i][n][4][4]:
                    continue
                maze.append(r_sqrs[i][n])
                func(maze)
                maze.pop()
            vis[i] = False

func([])

if m == float('inf'):
    print(-1)
else:
    print(m)