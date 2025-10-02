def solution(msg):
    dic = {chr(i):i-64 for i in range(ord('A'),ord('Z')+1)}
    
    start, end, state = 0, 1, 27
    length = len(msg)
    answer = []
    while start < length:
        while end <= length and dic.get(msg[start:end]):
            end += 1
        # 빠져 나오면
        if end <= length:
            dic[msg[start:end]] = state
            state += 1
        answer.append(dic[msg[start:end-1]])
        # 다음 루프는 end-1
        start = end-1
    
    return answer