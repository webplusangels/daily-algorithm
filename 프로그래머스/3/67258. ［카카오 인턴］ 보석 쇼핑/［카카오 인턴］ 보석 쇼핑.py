from collections import defaultdict

def solution(gems):
    gem_num = len(set(gems))
    answer = [1, len(gems)]
    
    s = e = 0
    gem_counts = defaultdict(int)
    while e < len(gems):
        gem_counts[gems[e]] += 1
        e += 1
        # gems[s:e]
        while len(gem_counts) == gem_num:
            # print(gem_counts, e, s)

            if answer[1] - answer[0] > e - s - 1:
                answer = [s+1, e]
            
            # print(answer)
            gem_counts[gems[s]] -= 1
            if gem_counts[gems[s]] == 0:
                gem_counts.pop(gems[s])
            s += 1
            
    return answer