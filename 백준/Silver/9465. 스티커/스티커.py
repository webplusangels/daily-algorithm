import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]
    for i in range(1, n):
        # 2개의 행 선택
        for j in range(2):
            # 최대 이전 2개 열까지 선택
            for k in range(max(0, i-2), i):
                for l in range(2):
                    if k == i-1 and l == j:
                        continue
                    dp[j][i] = max(dp[j][i], dp[l][k]+stickers[j][i])

    print(max(dp[0][n-1], dp[1][n-1]))