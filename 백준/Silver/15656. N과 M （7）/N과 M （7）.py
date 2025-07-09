import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()

def func(l):
    if len(l) == M:
        print(*l)
        return

    for n in N_list:
        l.append(n)
        func(l)
        l.pop()

func([])