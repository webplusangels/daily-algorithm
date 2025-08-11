import sys
input = lambda: sys.stdin.readline().rstrip()

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(l):
    level = l[0]
    spaces = -1
    for i in range(1, len(l)):
        diff = l[i] - level
        if diff:
            if abs(diff) > 1 or spaces > 0:
                return False
            if diff == 1:
                if -spaces < L:
                    return False
                spaces = 0
            if diff == -1:
                spaces = L
            level = l[i]
        spaces -= 1
    if spaces > 0:
        return False
    return True
    
cnt = 0
for i in range(N):
    lst = board[i][:]
    if check(lst):
        cnt += 1

for i in range(N):
    lst = [board[j][i] for j in range(N)]
    if check(lst):
        cnt += 1

print(cnt)