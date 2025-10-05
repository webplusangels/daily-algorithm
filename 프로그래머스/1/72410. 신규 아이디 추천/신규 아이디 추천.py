def solution(new_id):
    nid = []
    allowed = set(['-', '_', '.'])
    
    for s in new_id:
        # 2단계
        if not (s.isalpha() or s.isdigit() or s in allowed):
            continue
        
        # 3단계
        if nid and nid[-1] == '.' and s == '.':
            continue
        
        # 4단계
        if not nid and s == '.':
            continue

        # 1단계
        if s.isupper():
            s = s.lower()
            
        nid.append(s)
    
    if not nid: # 5단계
        nid = ['a']
    
    while nid[-1] == '.':  # 4단계 추가
        nid.pop()
    
    if len(nid) >= 16: # 6단계
        nid = nid[:15]
        while nid[-1] == '.':
            nid.pop()
    
    if len(nid) < 3: # 7단계
        nid = nid + [nid[-1]]*(3-len(nid))

    return ''.join(nid)