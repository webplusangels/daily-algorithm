import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
sums = [A[0]] + [0]*(N-1)

for i in range(1, N):
    m = 0
    for j in range(0, i):
        if A[j] < A[i]:
            m = max(m, sums[j])
    sums[i] = m + A[i]

print(max(sums))