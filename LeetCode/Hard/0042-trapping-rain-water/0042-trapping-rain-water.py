class Solution:
    def trap(self, height: List[int]) -> int:
        # 왼 오 기둥이 물을 가둘 가능성이 있을 때
        # 두 기둥 중 작은 기둥 기준으로 두 기둥 사이의
        # 물 용량을 계산함 (stack 활용)
        len_h = len(height)
        arr = [float('inf')] * len_h

        left_mx = 0
        for i in range(len_h):
            # 현재 최댓값
            left_mx = max(left_mx, height[i])

            # arr 갱신
            arr[i] = min(left_mx, arr[i])
        
        water = 0
        right_mx = 0
        for i in range(len_h-1, -1, -1):
            # 현재 최댓값
            right_mx = max(right_mx, height[i])

            # arr 갱신
            arr[i] = min(right_mx, arr[i])
            
            # 계산
            water += arr[i] - height[i]
        
        return water