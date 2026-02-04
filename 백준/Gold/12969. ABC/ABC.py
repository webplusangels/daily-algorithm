import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

# A와 B, C의 상태를 추적하면서 하나씩 추가했을 때의 개수 세기

memo = {}
def func(string, A, B, C, n):
    if A+B+C == N:
        if n == K:
            print(string)
            sys.exit()
        return

    if (A, B, C, n) in memo:
        return
    memo[(A, B, C, n)] = True
    
    func(string + 'A', A+1, B, C, n)
    func(string + 'B', A, B+1, C, n + A)
    func(string + 'C', A, B, C+1, n + (A+B))

func('', 0, 0, 0, 0)
print(-1)