import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
ns = [int(input()) for _ in range(n)]
m = min(ns)

dp = [0]*(k+1)
dp[0] = 1

for N in ns:
    for i in range(N, k+1):
        dp[i] = dp[i] + dp[i-N]
        # 처음엔 하나로만 쌓다가, 동전이 바뀌면 섞기 시작

print(dp[k])