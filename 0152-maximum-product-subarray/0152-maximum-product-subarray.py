class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        
        max_ = min_ = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            temp_max = max(num, max_ * num, min_ * num)
            min_ = min(num, max_ * num, min_ * num)
            
            max_ = temp_max
            
            result = max(result, max_)
            
        return result