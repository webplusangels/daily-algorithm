import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
sums = sum(map(sum, A))
diff = float('inf')

for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(N):
            for y in range(N):
                if d1+d2+x >= N:
                    continue
                if y-d1 < 0 or y+d2 >= N:
                    continue

                dims = [0]*5
                tmp_board = [[0]*N for _ in range(N)]
                for i in range(d1+1):
                    tmp_board[x+i][y-i] = 5
                    tmp_board[x+d2+i][y+d2-i] = 5
                for i in range(d2+1):
                    tmp_board[x+i][y+i] = 5
                    tmp_board[x+d1+i][y-d1+i] = 5

                for r in range(x+d1):
                    for c in range(y+1):
                        if tmp_board[r][c] == 5:
                            break
                        dims[0] += A[r][c]

                for r in range(x+d2+1):
                    for c in range(N-1, y, -1):
                        if tmp_board[r][c] == 5:
                            break
                        dims[1] += A[r][c]

                for r in range(x+d1, N):
                    for c in range(y-d1+d2):
                        if tmp_board[r][c] == 5:
                            break
                        dims[2] += A[r][c]

                for r in range(x+d2+1, N):
                    for c in range(N-1, y-d1+d2-1, -1):
                        if tmp_board[r][c] == 5:
                            break
                        dims[3] += A[r][c]

                dims[4] = sums - sum(dims)
                diff = min(diff, max(dims) - min(dims))
print(diff)