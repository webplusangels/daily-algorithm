import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
pqs = []
for i in range(N):
    p, q = map(int, input().split())
    pqs.append((p, i))
    pqs.append((-q, i))
    
pqs.sort(key=lambda x: abs(x[0]))
history = []
seat = {} # n번 손님: N번째 자리 
available = [] # 가장 작은 자리 pop (heapq)
p = 0

# [(10, 1), (20, 0), (30, 2), (-50, 0), (60, 3), ... ]
for pq in pqs:
    time, n = pq # 시간, 손님
    if time >= 0:
        if not available:
            seat[n] = p
            history.append(1)
            p += 1
        else:
            a = heapq.heappop(available)
            seat[n] = a
            history[a] += 1
    else:
        freed = seat.pop(n)
        heapq.heappush(available, freed)

print(p)
print(*history)