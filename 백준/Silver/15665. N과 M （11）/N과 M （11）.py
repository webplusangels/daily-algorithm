import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()

def func(l):
    if len(l) == M:
        print(*l)
        return

    last_num = None

    for i in range(N):
        if last_num != N_list[i]:
            l.append(N_list[i])
            last_num = N_list[i]
            func(l)
            l.pop()

func([])