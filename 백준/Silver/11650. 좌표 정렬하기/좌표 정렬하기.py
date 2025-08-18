import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = [list(map(int, input().split())) for _ in range(N)]

ns.sort(key = lambda x: (x[0], x[1]))

[print(*n) for n in ns]