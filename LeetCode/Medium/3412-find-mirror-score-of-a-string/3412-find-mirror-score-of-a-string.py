from collections import defaultdict

class Solution:
    def calculateScore(self, s: str) -> int:
        alpha = defaultdict(int)
        idx = defaultdict(list)
        cnt = 0
        for i, char in enumerate(s):
            char_num = ord(char)
            print(char_num)
            if not alpha[char_num-109.5]:
                alpha[109.5-char_num] += 1
                idx[109.5-char_num].append(i)
            else:
                alpha[char_num-109.5] -= 1
                j = idx[char_num-109.5].pop()
                cnt += i - j
    
        return cnt