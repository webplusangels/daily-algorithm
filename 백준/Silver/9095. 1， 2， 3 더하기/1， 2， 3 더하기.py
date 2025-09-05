import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0]*12
    arr[1], arr[2], arr[3] = 1, 2, 4
    for i in range(4, n+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    print(arr[n])