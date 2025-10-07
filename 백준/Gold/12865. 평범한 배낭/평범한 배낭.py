import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
emnts = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(K+1)

for w, v in emnts:
    for k in range(K, w-1, -1):
        dp[k] = max(dp[k], dp[k-w] + v)

print(dp[K])