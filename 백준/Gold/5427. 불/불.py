from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(bldg, vis, w, h):
    fire = []
    vis_sg = [[True for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if bldg[i][j] == '@':
                sg = (i, j, 0)
                vis_sg[i][j] = False
            elif bldg[i][j] == '*':
                fire.append((i, j))
                vis[i][j] = 0
                
    dq_fire = deque(fire)
    dq_sg = deque([sg])

    while dq_fire:
        fire_x, fire_y = dq_fire.popleft()
        for i in range(4):
            xx = dx[i] + fire_x
            yy = dy[i] + fire_y
            if 0 <= xx < h and 0 <= yy < w and bldg[xx][yy] != '#' and \
                vis[xx][yy] == -1:
                vis[xx][yy] = vis[fire_x][fire_y] + 1
                dq_fire.append((xx, yy))

    while dq_sg:
        sg_x, sg_y, run = dq_sg.popleft()
        if sg_x == 0 or sg_y == 0 or sg_x == h-1 or sg_y == w-1:
            return run+1
        for i in range(4):
            xx = dx[i] + sg_x
            yy = dy[i] + sg_y
            if 0 <= xx < h and 0 <= yy < w and bldg[xx][yy] != '#' and \
                vis_sg[xx][yy] and \
                (run+1 < vis[xx][yy] or vis[xx][yy] == -1):
                vis_sg[xx][yy] = False
                dq_sg.append((xx, yy, run+1))

    return 'IMPOSSIBLE'

for _ in range(T):
    w, h = map(int, input().split())
    bldg = []
    for _ in range(h):
        bldg.append(list(input()))
    vis = [[-1 for _ in range(w)] for _ in range(h)]
    print(bfs(bldg, vis, w, h))