import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N, K, M = map(int, input().split())
hypertube = [list(map(int, input().split())) for _ in range(M)]

if N == 1:
    print(1)
else:
    graph = {n: [] for n in range(1, N+M+1)}
    
    for i, ht in enumerate(hypertube):
        for station in ht:
            graph[station].append(N+i+1)
            graph[N+i+1].append(station)
    
    dq = deque([(1, 0)])
    visited = set([1])
    cnt = 0
    while dq:
        to_move, moved = dq.popleft()
        if to_move == N:
            cnt = moved
            break
    
        for nxt in graph[to_move]:
            if nxt in visited:
                continue
    
            dq.append((nxt, moved+1))
            visited.add(nxt)
    
    if cnt == 0:
        print(-1)
    else:
        print(cnt//2 + 1)