from collections import Counter

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # 이진수로 각 자리에서 1이 짝수개인 subarray를 구하라
        acc = [0]
        for i in range(len(nums)):
            acc.append(acc[i]^nums[i])
        
        counter = Counter(acc)
        answer = 0
        for v in counter.values():
            if v > 1:
                answer += v*(v-1)//2

        return answer