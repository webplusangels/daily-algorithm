import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
cheeses = input().split()

cheese_set = set(cheeses)
l = 0
for c in cheese_set:
    if c.endswith('Cheese'):
        l += 1

if l < 4:
    print('sad')
else:
    print('yummy')