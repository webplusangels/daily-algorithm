import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf')]*3 for _ in range(N)]
dp[0] = costs[0]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            
            new_cost = dp[i-1][j] + costs[i][k]
            dp[i][k] = min(dp[i][k], new_cost)

print(min(dp[N-1]))