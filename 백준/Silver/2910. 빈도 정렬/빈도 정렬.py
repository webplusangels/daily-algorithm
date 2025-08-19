import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N, C = input().split()
ns = list(map(int, input().split()))

counter = sorted(Counter(ns).items(), key=lambda x: x[1], reverse=True)
answer = []
for c in counter:
    for _ in range(c[1]):
        answer.append(c[0])

print(*answer)