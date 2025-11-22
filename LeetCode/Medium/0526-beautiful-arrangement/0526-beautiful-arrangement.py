from itertools import permutations

class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [[0]*(2**n) for _ in range(n+1)]

        for i in range(n):
            dp[1][1<<i] += 1
        
        for i in range(1, n):
            for j in range(1, 2**n):
                if dp[i][j] == 0:
                    continue
                
                for k in range(n):
                    if not (j & (1 << k)) and not ((i+1) % (k+1) and (k+1) % (i+1)):
                        dp[i+1][j ^ (1 << k)] += dp[i][j]
        
        return sum(dp[n])