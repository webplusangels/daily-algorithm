import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
INF = float('inf')

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

for i in range(N):
    for j in range(N):
        if board[i][j] != 0: continue
        
        cliffs = []
        for n in range(4):
            ni, nj = i+dx[n], j+dy[n]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 1: 
                cliffs.append(True)
            else:
                cliffs.append(False) 
        
        if (cliffs[1] or cliffs[3]) and (cliffs[0] or cliffs[2]):
            board[i][j] = -1 

heap = []
# (time, x, y, on_bridge, used)
heapq.heappush(heap, (0, 0, 0, False, 0)) 

# dist[x][y][on_bridge][used]
# on_bridge: 0(직전 땅), 1(직전 다리)
# used: 0(미사용), 1(사용)
dist = [[[[INF] * 2 for _ in range(2)] for _ in range(N)] for _ in range(N)]
dist[0][0][0][0] = 0

while heap:
    time, x, y, on_bridge, used = heapq.heappop(heap)

    # 도착
    if x == N-1 and y == N-1:
        print(time)
        break

    if dist[x][y][int(on_bridge)][used] < time:
        continue

    for n in range(4):
        nx, ny = x+dx[n], y+dy[n]
        
        if nx < 0 or nx >= N or 0 > ny or ny >= N or board[nx][ny] == -1:
            continue
        
        if board[nx][ny] == 1:
            new_time = time + 1
            if new_time < dist[nx][ny][0][used]:
                dist[nx][ny][0][used] = new_time
                heapq.heappush(heap, (new_time, nx, ny, False, used))
        
        else:
            # 연속으로 다리 건너기 불가
            if on_bridge:
                continue

            if board[nx][ny] == 0: 
                if used == 0:
                    period = M
                    if (time + 1) % period == 0:
                        new_time = time + 1
                    else:
                        new_time = (time + 1) + (period - (time + 1) % period)
                    
                    if new_time < dist[nx][ny][1][1]:
                        dist[nx][ny][1][1] = new_time
                        heapq.heappush(heap, (new_time, nx, ny, True, 1))
            
            elif board[nx][ny] > 1:
                period = board[nx][ny]
                if (time + 1) % period == 0:
                    new_time = time + 1
                else:
                    new_time = (time + 1) + (period - (time + 1) % period)
                
                if new_time < dist[nx][ny][1][used]:
                    dist[nx][ny][1][used] = new_time
                    heapq.heappush(heap, (new_time, nx, ny, True, used))