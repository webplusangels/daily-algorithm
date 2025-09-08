import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [0]*(N+1)
dq = deque([1])
while dq:
    x = dq.popleft()
    xs = [x+1, x*2, x*3]

    for n in xs:
        if n > N or arr[n]:
            continue
        else:
            arr[n] = x
            dq.append(n)
            
    if N in xs:
        break
    else:
        x += 1

t = [N]
while t[-1] != 1:
    t.append(arr[t[-1]])

print(len(t) - 1)
print(*t)