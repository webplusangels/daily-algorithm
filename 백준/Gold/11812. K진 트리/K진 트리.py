import sys
input = lambda: sys.stdin.readline().rstrip()

N, K, Q = map(int, input().split())

for _ in range(Q):
    x, y = map(int, input().split())
    
    if K == 1:
        print(abs(x - y))
        continue

    nx, ny = x - 1, y - 1
    cnt = 0
    
    while nx != ny:
        if nx > ny:
            nx = (nx - 1) // K
        else:
            ny = (ny - 1) // K
        
        cnt += 1
        
    print(cnt)