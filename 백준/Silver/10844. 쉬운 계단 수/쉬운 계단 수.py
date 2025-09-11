import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [[0]*10 for _ in range(101)]
dp[1] = [0] + [1]*9
NUM = 1000000000

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i+1][1] += dp[i][0] % NUM
        elif j == 9:
            dp[i+1][8] += dp[i][9] % NUM
        else:
            dp[i+1][j+1] += dp[i][j] % NUM
            dp[i+1][j-1] += dp[i][j] % NUM

print(sum(dp[N]) % NUM)