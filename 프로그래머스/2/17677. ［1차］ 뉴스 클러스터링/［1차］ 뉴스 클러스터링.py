def solution(str1, str2):
    def slide(s):
        from collections import Counter
        
        l = len(s)
        partial_set = []
        for i in range(l-1):
            new = s[i:i+2]
            if new.isalpha():
                partial_set.append(new.lower())
        
        return Counter(partial_set)
        
    sim_1 = slide(str1)
    sim_2 = slide(str2)
    
    if not sim_1 and not sim_2:
        return 65536
    
    print(f'{sim_1=} {sim_2=}')
    
    sim_u = 0
    sim_i = 0
    
    for e in set(sim_1) | set(sim_2):
        s1, s2 = sim_1.get(e, 0), sim_2.get(e, 0)
        if s1 and s2:
            sim_i += min(s1, s2)
        sim_u += max(s1, s2)
        
    answer = int(65536 * (sim_i / sim_u))
    return answer

        
    # answer = int(sim * 65536)
    # return answer