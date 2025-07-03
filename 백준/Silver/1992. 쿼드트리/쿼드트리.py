import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
quad_tree = []

for _ in range(N):
    line = list(map(int, list(input())))
    quad_tree.append(line)

answer = []

def comp(row, col, n):
    num = quad_tree[row][col]
    
    if n == 1:
        answer.append(f'{quad_tree[row][col]}')
        return

    for r in range(row, row+n):
        for c in range(col, col+n):
            if num != quad_tree[r][c]:
                nn = n//2
                answer.append('(')
                comp(row, col, nn)
                comp(row, col+nn, nn)
                comp(row+nn, col, nn)
                comp(row+nn, col+nn, nn)
                answer.append(')')
                return

    answer.append(f'{num}')
    return

comp(0, 0, N)
print(''.join(answer))