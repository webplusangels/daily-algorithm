import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

def func(lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(N):
        lst.append(i+1)
        func(lst)
        lst.pop()

func([])