import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

dir = [(1, 0), (0, 1), (1, 1)]
dq = deque([(0, 0)])

vis = [[0]*M for _ in range(N)]
vis[0][0] = nums[0][0]

for x in range(N):
    for y in range(M):
        to_add = vis[x][y]
        for d in dir:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < N and 0 <= dy < M:
                candies = nums[dx][dy] + to_add
                if vis[dx][dy] < candies:
                    vis[dx][dy] = candies

print(vis[N-1][M-1])