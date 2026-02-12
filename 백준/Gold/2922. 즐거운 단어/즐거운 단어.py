import sys
import math
input = lambda: sys.stdin.readline().rstrip()

word = list(input())

answer = 0

# 모음, 자음, L의 여부, 현재 인덱스
def func(m, j, l, idx, num):
    global answer

    if m == 3 or j == 3:
        return
    
    if idx == len(word):
        if l:
            answer += num
        return

    s = word[idx].lower()

    if s == '_':
        # 모음
        func(m+1, 0, l, idx+1, num*5)
        # 자음
        func(0, j+1, True, idx+1, num)
        func(0, j+1, l, idx+1, num*20)
    elif s in {'a', 'e', 'i', 'o', 'u'}:
        func(m+1, 0, l, idx+1, num)
    elif s == 'l':
        func(0, j+1, True, idx+1, num)
    else:
        func(0, j+1, l, idx+1, num)
    
func(0, 0, False, 0, 1)
print(answer)