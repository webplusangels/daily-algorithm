import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
sched = [list(map(int, input().split())) for _ in range(N)]

sched.sort(key=lambda x: (x[1], x[0]))
pnt = time = cnt = 0

while pnt < N:
    if sched[pnt][0] >= time:
        cnt += 1
        time = sched[pnt][1]
    pnt += 1

print(cnt)