import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = {n:0 for n in range(1, 10001)}

for _ in range(N):
    ns[int(input())] += 1

for n in range(1, 10001):
    t = ns[n]
    for _ in range(t):
        print(n)