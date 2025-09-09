import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [[0, 0] for _ in range(N)]
dp[0] = [0, 1] # '1'이 존재

for i in range(1, N):
    dp[i] = [dp[i-1][0]+dp[i-1][1], dp[i-1][0]]

print(sum(dp[-1]))