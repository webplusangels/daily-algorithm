import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N, H = map(int, input().split())
H_acc = [0]*(H+2)
for i in range(N):
    v = int(input())
    if i % 2:
        # 위
        H_acc[H-v+1] += 1
        H_acc[H+1] -= 1
    else:
        # 아래
        H_acc[1] += 1
        H_acc[v+1] -= 1

# ob[0] < X <= ob[1]
# 장애물의 수: 구간의 수
obs = 0
min_obs = float('inf')
route = 0
for i in range(1, H+1):
    obs += H_acc[i]
    if obs == min_obs:
        route += 1
    elif obs < min_obs:
        min_obs = min(min_obs, obs)
        route = 1

print(min_obs, route)