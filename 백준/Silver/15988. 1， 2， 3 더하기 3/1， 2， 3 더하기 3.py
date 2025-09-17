import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
cases = [int(input()) for _ in range(T)]
m = max(cases)

dp = [0]*(m+1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, m+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for c in cases:
    print(dp[c])