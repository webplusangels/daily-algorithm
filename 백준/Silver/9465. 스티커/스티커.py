import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue
        
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
    dp[0][1], dp[1][1] = dp[1][0]+stickers[0][1], dp[0][0]+stickers[1][1]
    
    for i in range(2, n):
        dp[0][i] = stickers[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = stickers[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))

