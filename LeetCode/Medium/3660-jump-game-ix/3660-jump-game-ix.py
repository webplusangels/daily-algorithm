class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # 아마 O(N) -> 한 번만 순회
        # 현재 구간의 최댓값이 남은 오른쪽 구간의 최솟값보다 작거나 같다면 더 이상 오른쪽으로 이동할 수 없음
        # 따라서 현재의 최댓값을 기준으로 길이만큼 채워넣어야 함
        n = len(nums)
        mins = nums[:]
        for i in range(n-2, -1, -1):
            mins[i] = min(mins[i], mins[i+1])

        print(mins)
        answer = []
        mx = 0
        for i, num in enumerate(nums):
            mx = max(mx, num)
            if i == n-1 or mx <= mins[i+1]:
                answer.extend([mx]*(i+1-len(answer)))
                mx = 0
            
        print(answer)
        return answer