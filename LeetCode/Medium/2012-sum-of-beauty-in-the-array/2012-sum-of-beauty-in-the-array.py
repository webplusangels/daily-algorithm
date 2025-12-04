class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        # 복잡도 O(N)
        n = tmp = 0
        flag = True
        answer = 0
        for i in range(len(nums)):
            if nums[i] > tmp:
                if n == 2:
                    n -= 1
                    answer += 1
                tmp = nums[i]
                n += 1
            else:
                flag = False
                n = 1
                tmp = nums[i]
        
        if flag:
            answer *= 2
        
        return answer