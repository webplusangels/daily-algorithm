import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
shark = None
size = ate = 2
space = []
for i in range(N):
    tmp = list(map(int, input().split()))
    if not shark:
        for j in range(N):
            if tmp[j] == 9:
                shark = (i, j)
                tmp[j] = 0
    space.append(tmp)

dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
move = 0

def bfs():
    cnt = 0
    dq = deque()
    fishes = []
    vis = [[False]*N for _ in range(N)]
    dq.append(shark)

    while dq:
        cnt += 1
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for n in range(4):
                xx, yy = x + dx[n], y + dy[n]
                if 0 <= xx < N and 0 <= yy < N and not vis[xx][yy]:
                    if space[xx][yy] == 0 or space[xx][yy] == size:
                        vis[xx][yy] = True
                        dq.append((xx, yy))
                    elif 0 < space[xx][yy] < size:
                        # space[xx][yy] = 0
                        # return (xx, yy, cnt)
                        fishes.append((xx, yy))
        if fishes:
            fishes.sort(key=lambda x: (x[0], x[1]))
            a_x, a_y = fishes[0]
            space[a_x][a_y] = 0
            return (a_x, a_y, cnt)
        
targets = []
while True:
    answer = bfs()
    if not answer:
        print(move)
        break
    x, y, cnt = answer
    move += cnt
    ate -= 1
    if ate == 0:
        size += 1
        ate = size
    shark = (x, y)
    # print(f'{size=}')
    # print(x, y)
    # print(move)
    # print(*space, sep='\n')
    
    