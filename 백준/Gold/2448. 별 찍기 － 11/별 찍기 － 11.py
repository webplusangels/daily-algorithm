import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
length = (N//3*5 + (N//3-1))
board = [[' ']*length for _ in range(N)]

def tri(N, r, c):
    if N == 3:
        board[r][c] = '*'
        board[r+1][c-1] = '*'
        board[r+1][c+1] = '*'
        board[r+2][c-2] = '*'
        board[r+2][c-1] = '*'
        board[r+2][c] = '*'
        board[r+2][c+1] = '*'
        board[r+2][c+2] = '*'
        return
    n = N // 2
    tri(n, r, c)
    tri(n, r+n, c-n)
    tri(n, r+n, c+n)

tri(N, 0, length//2)
for l in board:
    print(''.join(l))