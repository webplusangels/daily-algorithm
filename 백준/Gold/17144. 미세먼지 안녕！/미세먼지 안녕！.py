import sys
input = lambda: sys.stdin.readline().rstrip()

R, C, T = map(int, input().split())
purify = []
board = []
for i in range(R):
    tmp = list(map(int, input().split()))
    if tmp[0] == -1:
        purify.append(i)
    board.append(tmp)

dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)

def spread():
    global board
    new_board = [board[i][:] for i in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] >= 5:
                amount = board[i][j] // 5
                for n in range(4):
                    xx, yy = i+dx[n], j+dy[n]
                    if 0 <= xx < R and 0 <= yy < C and board[xx][yy] != -1:
                        new_board[xx][yy] += amount
                        new_board[i][j] -= amount                        

    board = new_board

def purifier():
    u_side, d_side = (purify[0], 1), (purify[1], 1)
    purified = u_n = 0
    
    while u_side != (purify[0], 0):
        x, y = u_side
        board[x][y], purified = purified, board[x][y]
        xx, yy = x+dx[u_n], y+dy[u_n]
        if not (0 <= xx < R and 0 <= yy < C):
            u_n += 1
            xx, yy = x+dx[u_n], y+dy[u_n]
        u_side = (xx, yy)

    purified = d_n = 0
    while d_side != (purify[1], 0):
        x, y = d_side
        board[x][y], purified = purified, board[x][y]
        xx, yy = x+dx[d_n], y+dy[d_n]
        if not (0 <= xx < R and 0 <= yy < C):
            d_n = (d_n - 1) % 4
            xx, yy = x+dx[d_n], y+dy[d_n]
        d_side = (xx, yy)

for i in range(T):
    spread()
    purifier()

s = 0
for i in range(R):
    s += sum(board[i])

print(s+2)