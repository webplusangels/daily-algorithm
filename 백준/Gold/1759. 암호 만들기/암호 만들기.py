import sys
input = lambda: sys.stdin.readline().rstrip()

L, C = map(int, input().split())
Cs = input().split()
Cs.sort()

flag = False
l = []

def func(w):
    if len(l) == L:
        v = c = 0
        for char in l:
            if char in 'aeiou':
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:        
            print(''.join(l))
        return

    for i in range(w, C):
        l.append(Cs[i])
        func(i+1)
        l.pop()

func(0)