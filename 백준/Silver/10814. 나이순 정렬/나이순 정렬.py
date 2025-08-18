import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = {i: [] for i in range(1, 201)}

for _ in range(N):
    age, name = input().split()
    ns[int(age)].append(name)

for i in range(1, 201):
    if ns[i]:
        for name in ns[i]:
            print(i, name)