def solution(dartResult):
    scores = []
    state = ptr = 0
    length = len(dartResult)
    while ptr < length:
        if dartResult[ptr+1].isdigit():
            scores.append(10)
            ptr += 1
        else:
            scores.append(int(dartResult[ptr]))
        
        ptr += 1
        
        if dartResult[ptr] == 'D':
            scores[state] *= scores[state]
        elif dartResult[ptr] == 'T':
            scores[state] *= scores[state]*scores[state]
        
        ptr += 1
        if ptr < length:
            if dartResult[ptr] == '*':
                if state > 0:
                    scores[state-1] *= 2
                scores[state] *= 2
                ptr += 1
            elif dartResult[ptr] == '#':
                scores[state] *= -1
                ptr += 1
        
        state += 1

    return sum(scores)