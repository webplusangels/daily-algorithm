from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
dq = deque([(N, 0)])
vis = set([N])

while True:
    subin, cnt = dq.popleft()
    if subin == K:
        print(cnt)
        break
        
    subin_moved = subin*2
    if 0 <= subin_moved <= 100000 and subin_moved not in vis:
        vis.add(subin_moved)
        dq.appendleft((subin_moved, cnt))
    
    for subin_moved in [subin-1, subin+1]:
        if 0 <= subin_moved <= 100000 and subin_moved not in vis:
            vis.add(subin_moved)
            dq.append((subin_moved, cnt+1))
    