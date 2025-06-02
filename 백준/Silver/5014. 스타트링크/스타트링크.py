from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

F, S, G, U, D = map(int, input().split())

if S == G:
    print(0)
else:
    tower = [-1 for _ in range(F+1)]
    dq = deque([S])
    tower[S] = 0
    
    while dq:
        now = dq.popleft()
        if now == G:
            print(tower[now])
            break
        to = [now + U, now - D]
        for t in to:
            if 0 < t <= F and tower[t] == -1:
                dq.append(t)
                tower[t] = tower[now] + 1
    else:
        print("use the stairs")