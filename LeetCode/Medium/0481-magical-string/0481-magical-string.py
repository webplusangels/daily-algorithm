from collections import Counter

class Solution:
    def magicalString(self, n: int) -> int:
        # 매직 스트링: 1과 2로 이루어진 스트링 
        # 이 스트링의 1과 2의 개수를 나열해도 결과가 같음
        i = 3
        p = 2
        s = [1, 2, 2]
        dic = {1: 2, 2: 1}
        # 1이면 2, 2이면 1을 더해야 함
        # 번갈아서 들어가야 하나
        while i < n:
            to_append = dic[s[-1]]
            
            for _ in range(s[p]):
                s.append(to_append)
                i += 1
            
            p += 1
        
        counter = Counter(s[:n])
        return counter[1]