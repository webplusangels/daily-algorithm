import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()

def func(w, l):
    if len(l) == M:
        print(*l)
        return

    for i in range(w, N):
        l.append(N_list[i])
        func(i, l)
        l.pop()

func(0, [])