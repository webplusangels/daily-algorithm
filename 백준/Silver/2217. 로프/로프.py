import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort()
m = 0

for r in ropes:
    m = max(m, r*N)
    N -= 1

print(m)