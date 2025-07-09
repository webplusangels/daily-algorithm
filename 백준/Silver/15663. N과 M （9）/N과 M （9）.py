import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

vis = [False] * N
last_num = None
N_list.sort()

def func(l):
    last_num = None
    
    if len(l) == M:
        print(*l)
        return

    for i in range(N):
        if not vis[i] and N_list[i] != last_num:
            l.append(N_list[i])
            vis[i] = True
            last_num = N_list[i]
            func(l)
            l.pop()
            vis[i] = False

func([])