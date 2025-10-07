import heapq

def solution(board):
    SIZE = len(board)
    
    # 3차원 costs (x, y, 방향)
    costs = [[[float('inf')]*4 for _ in range(SIZE)] for _ in range(SIZE)]
    dx, dy = (0, -1, 1, 0), (1, 0, 0, -1)
    costs[0][0] = [0, 0, 0, 0]
    
    # 다익스트라
    pq = [(0, 0, 0, -1)] # cost, x, y, 방향
    
    while pq:
        cost, x, y, d = heapq.heappop(pq)
        
        if cost > costs[x][y][d]:
            continue
        
        for n in range(4):
            xx, yy = x+dx[n], y+dy[n]
            if d == n or d == -1:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
            if 0 <= xx < SIZE and 0 <= yy < SIZE and not board[xx][yy] and costs[xx][yy][n] > new_cost:
                costs[xx][yy][n] = new_cost
                added = (new_cost, xx, yy, n)
                heapq.heappush(pq, added)
    
    return min(costs[SIZE-1][SIZE-1])