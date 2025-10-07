def solution(s):
    l = len(s)
    m = l
    
    for size in range(1, l//2+1):
        string = ''
        chunk = s[0:size]
        tmp = [chunk, 1]
        for i in range(1, l//size):
            new_chunk = s[i*size:i*size+size]
            if chunk == new_chunk:
                tmp[-1] += 1
            else:
                while tmp:
                    popped = tmp.pop()
                    if popped == 1:
                        continue
                    string += f'{popped}'
                chunk = new_chunk
                tmp = [chunk, 1]
        else:
            while tmp:
                popped = tmp.pop()
                if popped == 1:
                    continue
                string += f'{popped}'                
        m = min(len(string)+(l%size), m)
        # print(string, m)
    return m
    