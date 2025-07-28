import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)
ord = list(map(int, input().split()))

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dice_w = deque([1, 3, 6, 4])
dice_l = deque([1, 5, 6, 2])
dice = [0, 0, 0, 0, 0, 0]

def west():
    dice_w.rotate(-1)
    dice_l[0], dice_l[2] = dice_w[0], dice_w[2]

def east():
    dice_w.rotate(1)
    dice_l[0], dice_l[2] = dice_w[0], dice_w[2]

def north():
    dice_l.rotate(-1)
    dice_w[0], dice_w[2] = dice_l[0], dice_l[2]

def south():
    dice_l.rotate(1)
    dice_w[0], dice_w[2] = dice_l[0], dice_l[2]

def soak(i, j):
    if board[i][j] == 0:
        board[i][j] = dice[dice_w[2]-1]
    else:
        dice[dice_w[2]-1], board[i][j] = board[i][j], 0

def func(l):
    i, j = x, y
    for n in range(len(l)):
        o = ord[n]
        if o == 1:
            if j+1 < M:
                j += 1
                east()
            else: continue
        elif o == 2:
            if 0 <= j-1:
                j -= 1
                west()
            else: continue
        elif o == 3:
            if 0 <= i-1:
                i -= 1
                north()
            else: continue
        elif o == 4:
            if i+1 < N:
                i += 1
                south()
            else: continue
        soak(i, j)
        print(dice[dice_l[0]-1])

func(ord)