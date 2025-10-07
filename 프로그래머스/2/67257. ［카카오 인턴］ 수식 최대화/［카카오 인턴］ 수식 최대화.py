from itertools import permutations
from collections import deque

def solution(expression):
    ops = ['*', '-', '+']
    splitted = []
    tmp = []
    # 쪼개기
    for i in range(len(expression)):
        x = expression[i]
        if x.isdigit():
            tmp.append(x)
        else:
            splitted.append(int(''.join(tmp)))
            splitted.append(x)
            tmp = []
    splitted.append(int(''.join(tmp)))
    
    m = 0
    for seq in permutations(ops, 3):
        # 100 - 60000 - 500 + 20
        calculated = deque(splitted)
        for o in seq:
            l = len(calculated)
            i = 0
            while i < l:
                popped = calculated.popleft()
                if popped == o:
                    n1 = calculated.pop()
                    n2 = calculated.popleft()
                    if o == '*':
                        tmp = n1 * n2
                    elif o == '+':
                        tmp = n1 + n2
                    elif o == '-':
                        tmp = n1 - n2
                    calculated.append(tmp)
                    i += 2
                else:
                    calculated.append(popped)
                    i += 1
        m = max(m, abs(calculated[-1]))
    
    return m