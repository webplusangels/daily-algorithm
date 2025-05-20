from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N, L = map(int, input().split())
A_list = list(map(int, input().split()))
D_list = []
dq = deque()
m = A_list[0]

for i in range(N):
    D = max(0, i - L)
    
    while dq and dq[0] < i - L + 1:
        dq.popleft()
    
    while dq and A_list[dq[-1]] >= A_list[i]:
        dq.pop()
    
    dq.append(i)
    D_list.append(A_list[dq[0]])
    
print(*D_list)