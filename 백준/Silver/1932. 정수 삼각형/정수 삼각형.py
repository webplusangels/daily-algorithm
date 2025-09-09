import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = [tri[0]]

for i in range(1, n):
    l = len(tri[i-1])
    dp.append([0]*(l+1))
    for j in range(l):
        dp[i][j] = max(dp[i][j], dp[i-1][j]+tri[i][j])
        dp[i][j+1] = max(dp[i][j+1], dp[i-1][j]+tri[i][j+1])

print(max(dp[-1]))