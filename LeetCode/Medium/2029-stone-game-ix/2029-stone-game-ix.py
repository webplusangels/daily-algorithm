from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones_c = Counter([stone%3 for stone in stones])
        thr = sum(stones_c.values())
        now = 0

        def add_stone(now, stones_count):
            if now == 1:
                if stones_count[1]:
                    stones_count[1] -= 1
                    now += 1
                elif stones_count[0]:
                    stones_count[0] -= 1
                else:
                    return -1
            
            elif now == 2:
                if stones_count[2]:
                    stones_count[2] -= 1
                    now = 1
                elif stones_count[0]:
                    stones_count[0] -= 1
                else:
                    return -1
            
            return now

        result = [False, False]

        if stones_c[1]:
            stones_count = stones_c.copy() 
            stones_count[1] -= 1
            
            left = 1
            now = 1
            while left < thr:
                now = add_stone(now, stones_count)
                if now == -1:
                    result[0] = bool(left % 2)
                    break
                left += 1

        if stones_c[2]:
            stones_count = stones_c.copy()
            stones_count[2] -= 1
            
            left = 1
            now = 2
            while left < thr:
                now = add_stone(now, stones_count)
                if now == -1:
                    result[1] = bool(left % 2)
                    break
                left += 1
            
        if result[0] == True or result[1] == True:
            return True
        else:
            return False