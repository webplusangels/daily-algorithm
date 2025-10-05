from itertools import permutations

def solution(user_id, banned_id):
    l = len(banned_id)
    b_l = [len(bid) for bid in banned_id]
    cnt = []
    for c in permutations(user_id, l):
        if set(c) in cnt:
            continue
            
        flag = False
        for i in range(l): # 조합 하나 하나 비교
            if b_l[i] != len(c[i]):
                break
            
            for j in range(b_l[i]):
                if banned_id[i][j] == '*':
                    continue
                if banned_id[i][j] != c[i][j]:
                    flag = True
                    break
            if flag:
                break
        else:
            cnt.append(set(c))
               
    return len(cnt)