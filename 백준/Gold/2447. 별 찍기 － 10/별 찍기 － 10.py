import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [[' '] * N for _ in range(N)]

def star(N, r, c):
    if N == 1:
        board[r][c] = '*'
        return
    n = N // 3
    star(n, r, c)
    star(n, r, c+n)
    star(n, r, c+2*n)
    star(n, r+n, c)
    # star(N//3, r, c)
    star(n, r+n, c+2*n)
    star(n, r+2*n, c)
    star(n, r+2*n, c+n)
    star(n, r+2*n, c+2*n)

star(N, 0, 0)
for l in board:
    print(''.join(l))