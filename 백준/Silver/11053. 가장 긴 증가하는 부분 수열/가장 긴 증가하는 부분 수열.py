import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

pts = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            pts[i] = max(pts[i], pts[j]+1)

print(max(pts))