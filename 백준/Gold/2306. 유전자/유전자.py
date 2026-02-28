import sys
input = lambda: sys.stdin.readline().rstrip()

S = input()
N = len(S)
dp = [[0] * N for _ in range(N)]

for d in range(1, N):
    for i in range(N - d):
        j = i + d
        
        if (S[i] == 'a' and S[j] == 't') or (S[i] == 'g' and S[j] == 'c'):
            dp[i][j] = dp[i+1][j-1] + 2
        
        for k in range(i, j):
            if dp[i][j] < dp[i][k] + dp[k+1][j]:
                dp[i][j] = dp[i][k] + dp[k+1][j]

print(dp[0][N-1])