import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))

dp = [0]*(N+1)
mx = 0

for i in range(N):
    dp[nums[i]] = dp[nums[i]-1] + 1
    mx = max(mx, dp[nums[i]])

print(N-mx)