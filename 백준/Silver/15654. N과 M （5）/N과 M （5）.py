import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
vis = [False] * N

N_list.sort()

def func(l):
    if len(l) == M:
        print(*l)
        return

    for i in range(N):
        if not vis[i]:
            l.append(N_list[i])
            vis[i] = True
            func(l)
            l.pop()
            vis[i] = False

func([])