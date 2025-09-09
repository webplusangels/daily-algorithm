import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ns = list(map(int, input().split()))

cur_max = cur = ns[0]
for i in range(1, n):
    cur = max(cur+ns[i], ns[i])
    cur_max = max(cur_max, cur)

print(cur_max)