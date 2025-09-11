import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
sticks = list(map(int, input().split()))

sticks.sort(reverse=True)
long = sum(sticks)
cost = 0

while sticks:
    num = sticks.pop()
    long -= num
    cost += long*num

print(cost)