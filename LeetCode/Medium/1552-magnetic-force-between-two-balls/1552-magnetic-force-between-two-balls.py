class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = len(position)

        if m == 2:
            return position[-1] - position[0]

        def check(n):
            # n 거리 배치가 가능한가
            ball_pos = 0
            i = cnt = 1
            while i < l:
                if position[i]-position[ball_pos] >= n:
                    cnt += 1
                    ball_pos = i
                
                if cnt >= m:
                    return True
                i += 1
            else:
                return False

        left = 1
        right = position[-1] - position[0]
        answer = 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                answer = max(mid, answer)
                left = mid+1
            else:
                right = mid-1

        return answer