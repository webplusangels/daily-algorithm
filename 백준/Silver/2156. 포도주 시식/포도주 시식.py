import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
vino = [int(input()) for _ in range(n)]

# 얼마나 마셨는지, 몇 잔 연속(0/1/2)인지 상태를 기록
dp = [[0]*3 for _ in range(n)]
dp[0][1] = vino[0]

for i in range(n-1):
    dp[i+1][0] = max(dp[i][0], dp[i][1], dp[i][2])
    dp[i+1][1] = dp[i][0] + vino[i+1]
    dp[i+1][2] = dp[i][1] + vino[i+1]
    
print(max(dp[n-1]))