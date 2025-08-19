import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = defaultdict(int)

for _ in range(N):
    ns[int(input())] += 1

sorted_ns = sorted(ns.items(), key=lambda x: (x[1], -x[0]))
print(sorted_ns[-1][0])