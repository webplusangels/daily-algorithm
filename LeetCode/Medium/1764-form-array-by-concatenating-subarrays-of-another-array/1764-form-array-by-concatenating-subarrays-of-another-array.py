class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        group_p = i = 0
        while i < len(nums) and group_p < len(groups):
            for j in range(len(groups[group_p])):
                if i+j >= len(nums):
                    break
                if groups[group_p][j] != nums[i+j]:
                    break
            else:
                i = i + len(groups[group_p]) - 1
                group_p += 1
            i += 1
        
        if group_p == len(groups):
            return True
        else:
            return False