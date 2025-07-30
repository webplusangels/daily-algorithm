import sys
input = lambda: sys.stdin.readline().rstrip()
get_ints = lambda: map(int, input().split())

N, M = get_ints()
r, c, d = get_ints()
board = [list(get_ints()) for _ in range(N)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
cnt = 0

while True:
    if board[r][c] == 0:
        cnt += 1
        board[r][c] = 2

    for n in range(4):
        d = (d - 1) % 4
        xx, yy = r + dx[d], c + dy[d]
        if 0 <= xx < N and 0 <= yy < M:
            if board[xx][yy] == 0:
                r, c = xx, yy
                break
    else:
        xx, yy = r - dx[d], c - dy[d]
        if 0 <= xx < N and 0 <= yy < M and board[xx][yy] != 1:
            r, c = xx, yy
        else:
            break

print(cnt)