import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

def check(b):
    if b[r-1][c-1] == k:
        return True
    else:
        return False

def sorrrt(l):
    count = Counter(l)
    if 0 in count:
        count.pop(0)
    srtd = sorted(count.items(), key=lambda x: (x[1], x[0]))
    srtd = [elm for tps in srtd for elm in tps]
    return srtd
    
def transform(b):
    R, C = len(b), len(b[0])
    m = 0
    trns = []
    if R >= C:
        for i in range(R):
            line = b[i][:]
            sorted_line = sorrrt(line)
            trns.append(sorted_line[:100])
            m = max(len(trns[-1]), m)
            # m x C 같은 배열 만든 뒤에 채워넣으면 될 것 같음 m <= 100
        new_board = [[0]*m for _ in range(R)]
        for i in range(R):
            new_board[i][:len(trns[i])] = trns[i]
    else:
        for j in range(C):
            line = [b[i][j] for i in range(R)]
            sorted_line = sorrrt(line)
            trns.append(sorted_line[:100])
            m = max(len(trns[-1]), m)
        new_board = [[0]*C for _ in range(m)]
        for j in range(C):
            l = len(trns[j])
            for i in range(m):
                if l > i:
                    new_board[i][j] = trns[j][i]
                else:
                    new_board[i][j] = 0
    return new_board

for n in range(101):
    R, C = len(board), len(board[0])
    if R >= r and C >= c and check(board):
        print(n)
        break
    board = transform(board)
else:
    print(-1)