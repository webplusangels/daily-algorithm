import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
arr = [[0]*2 for _ in range(N+1)]
arr[1] = [stairs[1], 0]

for i in range(2, N+1):
    # j가 0일 때는 현재 계단 하나, 1일 때는 계단 두 개를 밟은 것
    arr[i][0] = max(arr[i-2]) + stairs[i]
    arr[i][1] = arr[i-1][0] + stairs[i]

# print(*arr, sep='\n')

print(max(arr[N]))