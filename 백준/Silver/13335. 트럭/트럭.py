import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

weight, i, time = trucks[0], 1, 1
bridge = deque([0] * (w-1) + [trucks[0]])

while bridge:
    thr = bridge.popleft()
    weight -= thr
    if i < n:
        if weight+trucks[i] <= L:
            bridge.append(trucks[i])
            weight += trucks[i]
            i += 1
        else:
            bridge.append(0)
    time += 1

print(time)