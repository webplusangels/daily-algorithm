import sys
sys.setrecursionlimit(10**6)

def solution(n, info):
    vis = [0]*11
    answer = -1
    result = None
    apeach_score = sum([10-i for i, s in enumerate(info) if s])
    
    def func(i, score, a_score, left):
        nonlocal answer, result
        
        if i == 11 or left == 0:
            vis[10] += left
            diff = score - a_score
            
            if diff > answer:
                answer = diff
                result = vis[:]
            elif diff == answer and diff > 0:
                for index in range(10, -1, -1):
                    if vis[index] > result[index]:
                        result = vis[:]
                        break
                    elif vis[index] < result[index]:
                        break
                
            vis[10] -= left
            return
        
        if left > info[i]:
            to_score = info[i] + 1 # i에서 득점하기 위한 화살의 수
            vis[i] = to_score
            new_left = left - to_score
            new_score = score + (10-i)
            new_a_score =  a_score - (10-i) if info[i] else a_score
            func(i+1, new_score, new_a_score, new_left)
            vis[i] = 0
    
        func(i+1, score, a_score, left)

    func(0, 0, apeach_score, n)
    
    if answer <= 0:
        return [-1]
    
    return result    