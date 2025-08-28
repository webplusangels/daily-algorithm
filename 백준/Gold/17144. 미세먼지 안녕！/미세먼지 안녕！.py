import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

R, C, T = map(int, input().split())
purify = []
dusts = {}
board = []
for i in range(R):
    tmp = list(map(int, input().split()))
    if tmp[0] == -1:
        purify.append(i)
    for j in range(C):
        if tmp[j] > 0:
            dusts[(i, j)] = tmp[j]
    board.append(tmp)

dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)

def dust_spread():
    global dusts
    new_dusts = defaultdict(int)
    for (x, y), amount in dusts.items():
        if amount < 5:
            new_dusts[(x, y)] += amount
            continue
        board[x][y] -= amount
        dusted = amount // 5
        for n in range(4):
            xx, yy = x+dx[n], y+dy[n]
            if 0 <= xx < R and 0 <= yy < C and not board[xx][yy] == -1:
                amount -= dusted
                new_dusts[(xx, yy)] += dusted
                board[xx][yy] += dusted
        new_dusts[(x, y)] += amount
        board[x][y] += amount
    dusts = new_dusts

def purifier():
    u_side, d_side = (purify[0], 1), (purify[1], 1)
    purified = u_n = 0
    
    while u_side != (purify[0], 0):
        x, y = u_side
        if board[x][y]:
            dusts.pop((x, y))
        if purified:
            dusts[(x, y)] = purified
        board[x][y], purified = purified, board[x][y]
        xx, yy = x+dx[u_n], y+dy[u_n]
        if not (0 <= xx < R and 0 <= yy < C):
            u_n += 1
            xx, yy = x+dx[u_n], y+dy[u_n]
        u_side = (xx, yy)

    purified = d_n = 0
    while d_side != (purify[1], 0):
        x, y = d_side
        if board[x][y]:
            dusts.pop((x, y))
        if purified:
            dusts[(x, y)] = purified
        board[x][y], purified = purified, board[x][y]
        xx, yy = x+dx[d_n], y+dy[d_n]
        if not (0 <= xx < R and 0 <= yy < C):
            d_n = (d_n - 1) % 4
            xx, yy = x+dx[d_n], y+dy[d_n]
        d_side = (xx, yy)

for i in range(T):
    dust_spread()
    purifier()

s = 0
for i in range(R):
    s += sum(board[i])

print(s+2)