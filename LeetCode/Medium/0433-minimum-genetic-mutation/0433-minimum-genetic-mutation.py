from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        candidates = ['A', 'C', 'G', 'T']
        dq = deque([startGene])
        cnt = 0
        while dq:
            for _ in range(len(dq)):
                gene = dq.popleft()
                if gene == endGene:
                    return cnt
                for i in range(8):
                    for acgt in candidates:
                        mut = gene[:i] + acgt + gene[i+1:]
                        if mut in bank:
                            bank.remove(mut)
                            dq.append(mut)
            cnt += 1
    
        return -1