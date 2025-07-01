import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

ps = {-1:0, 0:0, 1:0}

# 좌표만 넘기게 수정
def slicing(row, col, N):
    first = paper[row][col]
    if N == 0:
        ps[first] += 1
        return
    for r in range(row, row + N):
        for c in range(col, col + N):
            if paper[r][c] != first:
                n = N // 3
                slicing(row, col, n)
                slicing(row, col+n, n)
                slicing(row, col+2*n, n)
                slicing(row+n, col, n)
                slicing(row+n, col+n, n)
                slicing(row+n, col+2*n, n)
                slicing(row+2*n, col, n)
                slicing(row+2*n, col+n, n)
                slicing(row+2*n, col+2*n, n)
                return
    else: # 모두 같다면
        ps[first] += 1
        return

slicing(0, 0, N)
print(ps[-1])
print(ps[0])
print(ps[1])