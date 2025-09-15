import sys
input = lambda: sys.stdin.readline().rstrip()

T, W = map(int, input().split())
tree = [int(input()) for _ in range(T)]

# (시간, 몇 번 움직였는지 - 홀수면 2, 짝수면 1에 위치)
dp = [[-1]*(W+1) for _ in range(T)]
dp[0][0] = tree[0] % 2 
dp[0][1] = (dp[0][0]+1) % 2

for i in range(T-1):
    t = tree[i+1]
    for j in range(W+1):
        if dp[i][j] == -1:
            continue

        tmp = t == j%2+1
        dp[i+1][j] = max(dp[i+1][j], dp[i][j]+int(tmp))
        if j < W:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+int(not tmp))

# print(*dp, sep='\n')
print(max(dp[T-1]))