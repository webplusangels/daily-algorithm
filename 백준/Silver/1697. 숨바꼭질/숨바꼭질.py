from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
dq = deque([[N, 0]])
vis = [False] * 100001
vis[N] = True

while dq:
    N_new, cnt = dq.popleft()
    if N_new == K:
        print(cnt)
        break
    
    if 0 < N_new*2 <= 100000 and not vis[N_new*2]:
        vis[N_new*2] = True
        dq.append([N_new*2, cnt+1])
    if N_new+1 <= 100000 and not vis[N_new+1]:
        vis[N_new+1] = True
        dq.append([N_new+1, cnt+1])
    if 0 <= N_new-1 and not vis[N_new-1]:
        vis[N_new-1] = True
        dq.append([N_new-1, cnt+1])
