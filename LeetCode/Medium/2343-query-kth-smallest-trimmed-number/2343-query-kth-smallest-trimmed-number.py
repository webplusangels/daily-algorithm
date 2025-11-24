from collections import defaultdict

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        split = [[[0, i] for i in range(len(nums))] for _ in range(len(nums[0]))]
        
        for idx, num in enumerate(nums):
            rev_num = reversed(num)
            for i, n in enumerate(rev_num):
                res = int(n)*(10**i)
                for lst in split[i:]:
                    lst[idx][0] += res
        
        for lst in split:
            lst.sort(key=lambda x: (x[0], x[1]))

        answer = []
        for query in queries:
            k, trim = query
            idx = split[trim-1][k-1][1]
            answer.append(idx)

        return answer