def solution(files):
    def splitter(name):
        head_flag = False
        HEAD = NUMBER = TAIL = ''
        for i in range(len(name)):
            if not name[i].isdigit() and not head_flag:
                HEAD += name[i]
            
            elif name[i].isdigit() and len(NUMBER) < 5:
                head_flag = True
                NUMBER += name[i]
            
            else:
                TAIL += name[i:]
                break
        
        return HEAD, NUMBER, TAIL
    
    srtd = []
    for i, file in enumerate(files):
        head, num, tail = splitter(file)
        
        head = head.lower()
        num = int(num)
        processed = (i, head, num)
        
        srtd.append(processed)
    
    srtd.sort(key=lambda x: (x[1], x[2], x[0]))
    
    answer = []
    for s in srtd:
        answer.append(files[s[0]])
        
    return answer