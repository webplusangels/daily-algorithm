import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
bosses = list(map(int, input().split()))
praises = [list(map(int, input().split())) for _ in range(m)]

# n과 m이 10만 -> 많아도 O(N)
# 누적합?
result = [0]*n
for praise in praises:
    i, w = praise
    result[i-1] += w

for i in range(1, n):
    boss = bosses[i] - 1
    result[i] += result[boss]

print(*result)