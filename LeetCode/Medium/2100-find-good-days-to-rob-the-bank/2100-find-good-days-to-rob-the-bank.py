from collections import deque

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        left = [0]
        right = [0]
        streak_l = streak_r = 0
        lefty = righty = security[0]
        for i in range(1, len(security)):
            if lefty >= security[i]:
                streak_l += 1
            else:
                streak_l = 0

            print(righty, security[i])
            if righty <= security[i]:
                streak_r += 1
            else:
                streak_r = 0

            left.append(streak_l)
            right.append(streak_r)

            lefty = righty = security[i]
        
        answer = []
        for i in range(time, len(security)-time):
            if left[i] >= time and right[i+time] >= time:
                answer.append(i)

        return answer