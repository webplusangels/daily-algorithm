from collections import deque

class Solution:
    def maxOperations(self, s: str) -> int:
        comp = []
        stacked = 0
        answer = 0
        tmp = ''
        for string in s:
            if string == tmp:
                comp[-1][1] += 1
            else:
                if tmp == '1':
                    stacked += comp[-1][1]
                    answer += stacked
                comp.append([string, 1])
                tmp = string
        
        return answer