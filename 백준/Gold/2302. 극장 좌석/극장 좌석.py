import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
vips = set([int(input()) for _ in range(M)])

dp = [0]*41
dp[1], dp[2] = 1, 2

for i in range(3, 41):
    dp[i] += dp[i-1] + dp[i-2]

i = answer = 1
while i <= N:
    tmp = 0
    while i not in vips and i <= N:
        tmp += 1
        i += 1
    else:
        if tmp >= 1:
            answer *= dp[tmp]
        i += 1

print(answer)