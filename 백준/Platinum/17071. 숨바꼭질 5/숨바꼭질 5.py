import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

if N == K:
    print(0)
    exit()

sis_move = 1
vis = [[-1] * 500001 for _ in range(2)]
vis[0][N] = 0
dq = deque([N])

# 수빈이가 먼저 도착해 있으면 된다 K <= sub
# 단 홀, 짝에 주의해야 (짝일때만 가능)
while dq and K+sis_move <= 500000:
    cnt = sis_move # 현재 몇 번째 턴인지
    t = cnt % 2
    K += sis_move
    sis_move += 1
    for _ in range(len(dq)):
        sub = dq.popleft()
        for sub_moved in (sub-1, sub+1, sub*2):
            if 0 <= sub_moved <= 500000 and vis[t][sub_moved] == -1:
                vis[t][sub_moved] = cnt
                dq.append(sub_moved)
    if vis[t][K] != -1 and vis[t][K] <= cnt:
        print(cnt)
        break
else:
    print(-1)