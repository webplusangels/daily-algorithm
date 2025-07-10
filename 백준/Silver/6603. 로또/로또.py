import sys
input = lambda: sys.stdin.readline().rstrip()

def func(idx):
    if len(l) == 6:
        print(*l)
        return

    for i in range(idx, k):
        l.append(S[i])
        func(i+1)
        l.pop()

while True:
    case = list(map(int, input().split()))
    if case != [0]:
        k, S = case[0], case[1:]
        l = []
        func(0)
        print()
        
    else:
        break
