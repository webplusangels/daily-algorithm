import sys
from collections import deque, defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
rooms = defaultdict(list)

for _ in range(M):
    x, y, a, b = map(int, input().split())
    rooms[(x, y)].append((a, b))

# 차례대로 pop하면서 deque에 삽입
dq = deque([(1, 1)])
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
light = [[False] * (N+1) for _ in range(N+1)]
vis = set([(1, 1)])
num_lgt = 1
light[1][1] = True

while dq:
    x, y = dq.popleft()
    
    # 불 키기
    for nxt_x, nxt_y in rooms[(x, y)]:
        if not light[nxt_x][nxt_y]:
            light[nxt_x][nxt_y] = True
            num_lgt += 1
            for n in range(4):
                xx, yy = dx[n] + nxt_x, dy[n] + nxt_y
                if 0 < xx <= N and 0 < yy <= N and (xx, yy) in vis:
                    dq.append((nxt_x, nxt_y))
                    vis.add((nxt_x, nxt_y))
                    break
                    
    # 방문
    for n in range(4):
        xx, yy = dx[n] + x, dy[n] + y
        if 0 < xx <= N and 0 < yy <= N and light[xx][yy] and (xx, yy) not in vis:
            dq.append((xx, yy))
            vis.add((xx, yy))

print(num_lgt)