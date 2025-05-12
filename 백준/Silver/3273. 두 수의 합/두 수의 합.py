import sys
from collections import defaultdict

input = sys.stdin.readline

_ = input().strip()
n_list = list(map(int, input().split()))
x = int(input().strip())

n_dict = defaultdict(int)
count = 0

for n in n_list:
    target = x - n
    if n_dict[n] == 1:
        count += 1
    else:
        n_dict[target] += 1

print(count)