class Solution:
    def minimumSteps(self, s: str) -> int:
        stacked = 0
        answer = 0
        for string in s:
            if string == '1':
                stacked += 1
            else:
                answer += stacked
        
        return answer
        