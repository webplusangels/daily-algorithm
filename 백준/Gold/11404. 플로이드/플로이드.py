import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
buses = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for bus in buses:
    frm, to, cost = bus
    graph[frm-1][to-1] = min(graph[frm-1][to-1], cost)
    
# 플로이드
for i in range(n):
    # i를 지나가는 녀석들의 최단거리를 계산해 업데이트
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == j or i == k or graph[j][k] == 0:
                continue
            updated = graph[j][i] + graph[i][k]
            graph[j][k] = min(updated, graph[j][k])
            
# 1 -> 2? 1 -> 0 -> 2 확인
for i in range(n):
    for j in range(n):
        if graph[i][j] == float('inf'):
            graph[i][j] = 0

for i in range(n):
    print(*graph[i])