import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
virus = []
lab = []
availables = N*N - M
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            virus.append((i, j))
        if tmp[j] == 1:
            availables -= 1
    lab.append(tmp)

# print(f'{virus=} {availables=}')
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs(w):
    vis = [[False]*N for _ in range(N)]
    for x, y in w:
        vis[x][y] = True
    dq = deque(w)
    time = -1
    cnt = 0

    # print(f'{dq=}')
    while dq:
        # time += 1
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for n in range(4):
                xx, yy = x+dx[n], y+dy[n]
                if 0 <= xx < N and 0 <= yy < N and not vis[xx][yy] and lab[xx][yy] != 1:
                    vis[xx][yy] = True
                    dq.append((xx, yy))
                    cnt += 1    
        time += 1
    
    if cnt != availables:
        return
    else:
        return time
                

num_virus = len(virus)
m = float('inf')
def func(w, num):
    global m
    if len(w) == M:
        answer = bfs(w)
        if answer != None:        
            m = min(m, answer)
        return

    for i in range(num, num_virus):
        w.append(virus[i])
        func(w, i+1)
        w.pop()

func([], 0)
if m == float('inf'):
    print(-1)
elif m == -1:
    print(0)
else: print(m)