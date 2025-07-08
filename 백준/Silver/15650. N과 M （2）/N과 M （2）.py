import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

def func(w, lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(w, N):
        lst.append(i+1)
        func(i+1, lst)
        lst.pop()

func(0, [])