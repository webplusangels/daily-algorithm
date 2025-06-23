import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
area = []
L = []
for i in range(R):
    line = list(input())
    for j, char in enumerate(line):
        if char == 'L':
            L.append((i, j))
            line[j] = '.'
    area.append(line)

dx, dy = (1, -1, 0 , 0), (0, 0, 1, -1)
vis = [[0] * C for _ in range(R)]
edges = set()
cnt = 0

for i in range(R):
    for j in range(C):
        dq = deque()
        if area[i][j] == '.' and not vis[i][j]:
            dq.append((i, j))
            cnt += 1
            vis[i][j] = cnt            
            while dq:
                x, y = dq.popleft()
                for n in range(4):
                    xx, yy = dx[n] + x, dy[n] + y
                    if 0 <= xx < R and 0 <= yy < C:
                        if area[xx][yy] == '.' and not vis[xx][yy]:
                            dq.append((xx, yy))
                            vis[xx][yy] = cnt
                        if area[xx][yy] == 'X':
                            edges.add((x, y))

dq_edges = deque(edges)
parent = list(range(cnt + 1))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def melt():
    next_dq = deque()
    len_dq = len(dq_edges)
    for _ in range(len_dq):
        x, y = dq_edges.popleft()
        for n in range(4):
            xx, yy = dx[n] + x, dy[n] + y
            if 0 <= xx < R and 0 <= yy < C and not vis[xx][yy]:
                vis[xx][yy] = vis[x][y]
                next_dq.append((xx, yy))

    while next_dq:
        x, y= next_dq.popleft()
        dq_edges.append((x, y))
        for n in range(4):
            xx, yy = dx[n] + x, dy[n] + y
            if 0 <= xx < R and 0 <= yy < C and vis[xx][yy] != 0 and vis[xx][yy] != vis[x][y]:
                if find(vis[x][y]) != find(vis[xx][yy]):
                    union(vis[x][y], vis[xx][yy])

answer = 0
L_1, L_2 = vis[L[0][0]][L[0][1]], vis[L[1][0]][L[1][1]]

if find(L_1) == find(L_2):
    print(0)
else:
    while True:
        # 하루를 보낸다
        melt()
        answer += 1
        
        # 하루를 보낸 후, 만났는지 확인한다
        if find(L_1) == find(L_2):
            print(answer)
            break