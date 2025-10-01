def solution(n, t, m, p):
    strs = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    state = 1
    lens = 0
    answer = ''
    numbers = '0'
    while lens < (t-1)*m + p:
        mok = state
        generated = ''
        while mok != 0:
            mok, nam = divmod(mok, n)
            if nam >= 10:
                nam = strs[nam]
            generated = str(nam) + generated
        numbers += generated
        lens += len(generated)
        state += 1

    for i in range(t):
        answer += numbers[i*m + p-1]
        
    return answer