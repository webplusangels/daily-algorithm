def solution(survey, choices):
    personality = 'RTCFJMAN'
    result = {k:0 for k in personality}
    for i in range(len(survey)):
        # [0]과 [1]을 choice를 기준으로 점수 측정
        s1, s2 = survey[i]
        choice = choices[i]
        if choice == 4:
            continue
        elif choice < 4:
            # 1일 때 3 2일 때 2 3일 때 1
            result[s1] += 4 - choice
        elif choice > 4:
            # 5일 때 1 6일 때 2 7일 때 3
            result[s2] += choice - 4
    
    answer = ''
    for i in range(4):
        p1, p2 = personality[i*2], personality[i*2+1]
        if result[p1] >= result[p2]:
            answer += p1
        else:
            answer += p2
    
    return answer