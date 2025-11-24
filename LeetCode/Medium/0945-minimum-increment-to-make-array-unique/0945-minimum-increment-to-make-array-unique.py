class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # O(n)에 끝내야 함
        dic = {}
        next_num = 0
        cnt = 0
        nums.sort()
        for n in nums:
            if dic.get(n):
                while next_num in dic or next_num < n:
                    next_num += 1
                cnt += next_num - n
                dic[next_num] = 1
                next_num += 1
            else:
                dic[n] = 1

        
        return cnt