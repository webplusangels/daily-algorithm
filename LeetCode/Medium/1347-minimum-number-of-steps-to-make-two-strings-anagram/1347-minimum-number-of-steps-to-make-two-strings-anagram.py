from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_ = Counter(s)
        t_ = Counter(t)

        result = s_ - t_

        return sum(result.values())