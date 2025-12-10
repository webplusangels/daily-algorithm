class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        sm_p = 0
        mid = (0 + l) // 2
        big_p = mid
        answer = 0

        # 조건이 만족하면 둘 다 전진, 만족하지 못하면 big_p만 전진
        while sm_p < mid and big_p < l:
            if nums[sm_p] * 2 <= nums[big_p]:
                sm_p += 1
                answer += 2
            big_p += 1
        
        return answer
