from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ln = len(rectangles)
        # 길이가 1일 때
        if ln == 1:
            return 0
        
        ratio = defaultdict(int)
        for recs in rectangles:
            w, h = recs
            ratio[w/h] += 1
        
        cnt = 0
        for v in ratio.values():
            cnt += (v*(v-1))//2
        
        return cnt