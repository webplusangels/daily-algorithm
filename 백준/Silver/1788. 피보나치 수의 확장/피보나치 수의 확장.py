import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
absn = abs(n)
isneg = absn != n
dp = [0, 1] + [0]*(absn-1)
NUM = 1000000000

if isneg:
    for i in range(2, absn+1):
        dp[i] = dp[i-2] - dp[i-1]
        if abs(dp[i]) > NUM:
            if dp[i] < 0:
                dp[i] = -(-dp[i] % NUM)
            else:
                dp[i] = dp[i] % NUM
else:
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % NUM


answer = dp[absn]
if answer < 0:
    print(-1)
    print(-answer)
elif answer > 0:
    print(1)
    print(answer)
else:
    print(0)
    print(0)