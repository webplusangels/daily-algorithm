import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort(reverse=True)

answer = 0
for i in range(N):
    answer += A[i]*B[i]

print(answer)