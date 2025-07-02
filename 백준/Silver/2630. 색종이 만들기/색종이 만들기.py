import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

borw = {0:0, 1:0}

def papercut(row, col, n):
    num = paper[row][col]
    if n == 1:
        borw[num] += 1
        return

    for r in range(row, row+n):
        for c in range(col, col+n):
            if num != paper[r][c]:
                nn = n // 2
                papercut(row, col, nn)
                papercut(row, col+nn, nn)
                papercut(row+nn, col, nn)
                papercut(row+nn, col+nn, nn)
                return

    borw[num] += 1
    return

papercut(0, 0, N)
print(borw[0])
print(borw[1])