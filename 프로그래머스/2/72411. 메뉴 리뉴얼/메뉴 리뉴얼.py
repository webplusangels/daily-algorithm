from collections import Counter, defaultdict
from itertools import combinations

def solution(orders, course):
    frq = defaultdict(int)
    
    for order in orders:
        for length in course:
            for c in combinations(order, length):
                comb = ''.join(sorted(c))
                frq[comb] += 1
    
    max_length = {k: ['', 0] for k in course}
    for k, v in frq.items():
        if v < 2:
            continue
        if max_length[len(k)][1] == v:
            max_length[len(k)][0] = max_length[len(k)][0] + [k]
        elif max_length[len(k)][1] < v:
            max_length[len(k)][0] = [k]
            max_length[len(k)][1] = v
        print(max_length)
    
    result = []
    for _, v in max_length.items():
        # print(k)
        result.extend(v[0])
        
    result.sort()
    return result