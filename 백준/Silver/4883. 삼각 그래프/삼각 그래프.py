import sys
input = lambda: sys.stdin.readline().rstrip()

T = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    costs = [[0]*3 for _ in range(N)]
    costs[0][1], costs[0][2] = graph[0][1], graph[0][1] + graph[0][2]
    costs[1][0] = costs[0][1] + graph[1][0]
    costs[1][1] = min(costs[0][1], costs[1][0], costs[0][2]) + graph[1][1]
    costs[1][2] = min(costs[0][1], costs[1][1], costs[0][2]) + graph[1][2]
    
    for i in range(2, N):
        costs[i][0] = min(costs[i-1][0], costs[i-1][1]) + graph[i][0]
        costs[i][1] = min(costs[i-1][0], costs[i-1][1], costs[i-1][2], costs[i][0]) + graph[i][1]
        costs[i][2] = min(costs[i-1][1], costs[i-1][2], costs[i][1]) + graph[i][2]

    costs[N-1][1] = min(costs[N-1][1], costs[N-1][0]+graph[N-1][1])
    
    # print(*costs, sep='\n')
    print(f"{T}. {costs[N-1][1]}")
    T += 1