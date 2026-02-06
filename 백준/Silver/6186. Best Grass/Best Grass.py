import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

vis = [[False]*C for _ in range(R)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
cnt = 0

for i in range(R):
    for j in range(C):
        if vis[i][j]:
            continue
        
        vis[i][j] = True

        if board[i][j] == '.':
            continue

        cnt += 1
        
        for n in range(4):
            xx, yy = i+dx[n], j+dy[n]
            if 0 <= xx < R and 0 <= yy < C and not vis[xx][yy]:
                if board[xx][yy] == '#':
                    vis[xx][yy] = True
                    break

print(cnt)