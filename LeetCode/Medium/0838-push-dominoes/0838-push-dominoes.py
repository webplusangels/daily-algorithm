from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 어떤 자료구조?
        to_do = deque()
        len_dom = len(dominoes)
        doms = ['.']*len_dom

        for i, dom in enumerate(dominoes):
            if dom == 'L' or dom == 'R':
                to_do.append((i, dom))
                doms[i] = dom
        
        while to_do:
            temp = {}
            # 넘어진 : F, 이번 턴에 넘어지는: ML/MR
            for _ in range(len(to_do)):
                n, dom = to_do.popleft()
                if dom == 'L':
                    if temp.get(n-1) == 'R':
                        del temp[n-1]
                    elif 0 < n and doms[n-1] == '.':
                        temp[n-1] = 'L'
                elif dom == 'R':
                    if temp.get(n+1) == 'L':
                        del temp[n+1]
                    elif n < len_dom-1 and doms[n+1] == '.':
                        temp[n+1] = 'R'
            
            for k, v in temp.items():
                to_do.append((k, v))
                doms[k] = v
            
        return ''.join(doms)