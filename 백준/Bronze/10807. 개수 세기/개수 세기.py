import sys
input = sys.stdin.readline

_ = input()
n_list = input().split()
v = input().strip()

from collections import Counter

counter = Counter(n_list)
print(counter[v])