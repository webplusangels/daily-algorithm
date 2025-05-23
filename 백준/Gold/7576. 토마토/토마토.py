from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

M, N = map(int, input().split())
tomatoes = []

for _ in range(N):
    line = list(map(int, input().split()))
    tomatoes.append(line)
    
max_day = 0
dq = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            # 가로, 세로, 날짜
            dq.append((i, j, 0))

else:
    while dq:
        # 깊이 우선 pop, 넓이 우선 popleft
        i, j, day = dq.popleft()
        if i+1 < N and not tomatoes[i+1][j]:
            dq.append((i+1, j, day+1))
            tomatoes[i+1][j] = 1
        if j+1 < M and not tomatoes[i][j+1]:
            dq.append((i, j+1, day+1))
            tomatoes[i][j+1] = 1
        if i-1 >= 0 and not tomatoes[i-1][j]:
            dq.append((i-1, j, day+1))
            tomatoes[i-1][j] = 1
        if j-1 >= 0 and not tomatoes[i][j-1]:
            dq.append((i, j-1, day+1))
            tomatoes[i][j-1] = 1
        max_day = max(day, max_day)
    
    for i in range(N):
        if not all(tomatoes[i]):
            print(-1)
            break
    else:
        print(max_day)