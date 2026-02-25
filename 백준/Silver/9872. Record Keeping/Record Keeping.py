import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dd = defaultdict(int)
for _ in range(N):
    grp = tuple(sorted(input().split()))
    dd[grp] += 1

v = sorted([v for v in dd.values()])
print(v[-1])