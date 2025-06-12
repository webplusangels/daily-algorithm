import sys
from collections import deque, defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

# route를 기록하는 list 격자를 만든다면...
dq = deque([N])
dist = [-1] * 100001
route = [-1] * 100001
dist[N] = 0

while dq:
    sub = dq.popleft()
    if sub == K:
        break
    to_go = [sub * 2, sub + 1, sub - 1]
    for r in to_go:
        if 0 <= r <= 100000 and dist[r] == -1:
            dist[r] = dist[sub] + 1
            route[r] = sub
            dq.append(r)

print(dist[K])

n = route[sub]
routes = [K]
while n != -1:
    routes.append(n)
    n = route[n]

print(*routes[::-1])