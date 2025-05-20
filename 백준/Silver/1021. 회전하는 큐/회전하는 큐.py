import sys
from collections import deque
input = sys.stdin.readline

N, M = input().split()
a_list = list(map(int, input().split()))

dq = deque(range(1, int(N)+1))
cnt = 0

for a in a_list:
    if a == dq[0]:
        dq.popleft()
    else:
        left_rotated = dq.copy()
        right_rotated = dq.copy()
        cur_cnt = 0
        while True:
            left_rotated.rotate(-1)
            right_rotated.rotate(1)
            cur_cnt += 1
            if left_rotated[0] == a:
                dq = left_rotated
                break
            elif right_rotated[0] == a:
                dq = right_rotated
                break
        dq.popleft()
        cnt += cur_cnt
        
print(cnt)