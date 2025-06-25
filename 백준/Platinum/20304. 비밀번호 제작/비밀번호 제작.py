import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 이진법
N = int(input())
M = int(input())
p = list(map(int, input().split()))

vis = set(p)
max_len = N.bit_length()
dq = deque(p)
cnt = 0

while dq:
    flag = False
    for _ in range(len(dq)):
        x = dq.popleft()
        for n in range(max_len):
            xx = x ^ (1 << n) # 변형된 값
            if xx <= N and xx not in vis:
                vis.add(xx)
                dq.append(xx)
                flag = True
    if not flag:
        print(cnt)
        break
    cnt += 1