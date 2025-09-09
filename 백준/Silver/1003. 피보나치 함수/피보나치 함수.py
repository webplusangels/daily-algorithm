import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
dp = [[1, 0], [0, 1]] + [[0, 0] for _ in range(40)]

for i in range(2, 40+1):
    for n in range(2):        
        dp[i][n] = dp[i-2][n] + dp[i-1][n]

for _ in range(T):
    N = int(input())
    print(*dp[N])