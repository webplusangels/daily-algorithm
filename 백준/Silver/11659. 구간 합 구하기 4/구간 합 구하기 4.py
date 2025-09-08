import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ns = list(map(int, input().split()))
ijs = [list(map(int, input().split())) for _ in range(M)]

sums = [0, ns[0]]+[0]*(N-1)
for i in range(1, N+1):
    sums[i] = sums[i-1] + ns[i-1]

for i, j in ijs:
    print(sums[j] - sums[i-1])