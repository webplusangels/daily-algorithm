import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, H = map(int, input().split())
lines = set()
for _ in range(M):
    line = list(map(int, input().split()))
    lines.add((line[0]-1, line[1]-1))
numbers = (N-1) * H

def coord(n):
    i, j = n // (N-1), n % (N-1)
    return (i, j)

def check(w):
    lns = lines | set(w)
    for s in range(N):
        now = s
        for d in range(H):
            if (d, now) in lns:
                now += 1
            elif (d, now-1) in lns:
                now -= 1
        if now != s:
            return False
    else:
        return True
        
flag = -1
def func(w, start, num):
    global flag
    if flag != -1:
        return
    
    if len(w) == num:
        if check(w):
            flag = num
        return

    for x in range(start, numbers):
        i, j = coord(x)
        if {(i, j), (i, j+1), (i, j-1)} & lines:
            continue
        w.append((i, j))
        func(w, x+1, num)
        w.pop()

for i in range(4):
    func([], 0, i)
    if flag != -1:
        print(flag)
        break
else:
    print(-1)