import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]

days = [0]*(N+1)

for i in range(N):
    t, p = TP[i]
    if i+t <= N:
        days[i+t] = max(days[i]+p, days[i+t]) 

    days[i+1] = max(days[i+1], days[i])

print(days[N])