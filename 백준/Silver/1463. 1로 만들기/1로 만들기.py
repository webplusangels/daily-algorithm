import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [0]*(N+1)

for i in range(2, N+1):
    arr[i] = 1 + arr[i-1]
    if not (i % 3):
        arr[i] = min(arr[i], arr[i//3]+1)
    if not (i % 2):
        arr[i] = min(arr[i], arr[i//2]+1)

print(arr[N])