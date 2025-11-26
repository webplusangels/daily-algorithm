from collections import defaultdict

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = defaultdict(int)
        for cand in candidates:
            binned = reversed(bin(cand)[2:])
            for i, b in enumerate(binned):
                if b == '1':
                    cnt[i] += 1

        return max(cnt.values())