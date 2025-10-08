from itertools import combinations

def solution(relation):
    columns = [] # column의 개수
    for i in range(len(relation[0])):
        tmp = [n[i] for n in relation]
        columns.append(tmp)
    
    key_list = []
    # 차례 차례 작은 집합부터 확인
    for i in range(1, len(columns)+1):
        for keys in combinations(range(len(columns)), i):
            # print(keys)
            og = [n for n in zip(*list(columns[key] for key in keys))]
            if len(og) != len(set(og)):
                continue
            else:
                key_list.append(set(keys))
    
    soldout = []
    answer = []
    print(key_list)
    # 서로 교집합이 있으면 안됨
    # 크기가 작은 set부터 넣고 비교
    for key in key_list:
        for so in answer:
            if so & key == so:
                break
        else:
            answer.append(key)
    
    return len(answer)