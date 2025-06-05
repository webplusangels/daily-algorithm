from sys import stdin
from collections import deque, defaultdict
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
ices = []

for _ in range(N):
    line = list(map(int, input().split()))
    ices.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 존재하는 빙산을 추적
ice_loc = set()
for i in range(N):
    for j in range(M):
        if ices[i][j] > 0:
            ice_loc.add((i, j))

def melt_per_year(ices, ice_loc):
    melt_amount = defaultdict(int)
    ice_return = [row[:] for row in ices]
    new_ice_loc = set()
    for ice in ice_loc:
        i, j = ice
        for n in range(4):
            xx = dx[n] + i
            yy = dy[n] + j
            if 0 <= xx < N and 0 <= yy < M and ices[xx][yy] == 0:
                melt_amount[(i, j)] += 1
                
        ice_temp = ices[i][j] - melt_amount[(i, j)]
        if ice_temp > 0:
            new_ice_loc.add((i, j))            
        ice_return[i][j] = max(0, ice_temp)    

    return ice_return, new_ice_loc

def bfs(ice_loc):
    i, j = ice_loc.pop()
    dq = deque([(i, j)])
    while dq:
        x, y = dq.popleft()
        for n in range(4):
            xx = dx[n] + x
            yy = dy[n] + y
            if (xx, yy) in ice_loc:
                ice_loc.remove((xx, yy))
                dq.append((xx, yy))

    if ice_loc:
        return False
    else:
        return True

year = 1
while True:
    ices, ice_loc = melt_per_year(ices, ice_loc)
    new_ice_loc = ice_loc.copy()
    if not ice_loc:
        print(0)
        break
    if bfs(new_ice_loc):
        year += 1
    else:
        print(year)
        break