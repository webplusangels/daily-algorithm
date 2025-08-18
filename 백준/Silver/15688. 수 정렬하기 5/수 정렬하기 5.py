import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = defaultdict(int)

for _ in range(N):
    ns[int(input())] += 1

ns = sorted(ns.items())

for i in range(len(ns)):
    value, times = ns[i]
    [print(value) for _ in range(times)]