import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ground = [[5] * N for _ in range(N)]

trees_board = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees_board[x - 1][y - 1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    dead_trees = []

    for r in range(N):
        for c in range(N):
            num_trees_in_cell = len(trees_board[r][c])
            for i in range(num_trees_in_cell):
                age = trees_board[r][c].popleft()
                if ground[r][c] >= age:
                    ground[r][c] -= age
                    trees_board[r][c].append(age + 1)
                else:
                    dead_trees.append((r, c, age))
    
    for r, c, age in dead_trees:
        ground[r][c] += age // 2

    new_trees = []
    for r in range(N):
        for c in range(N):
            for age in trees_board[r][c]:
                if age % 5 == 0:
                    for i in range(8):
                        nr, nc = r + dx[i], c + dy[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            new_trees.append((nr, nc))
    
    for r, c in new_trees:
        trees_board[r][c].appendleft(1)

    for r in range(N):
        for c in range(N):
            ground[r][c] += A[r][c]

total_trees = 0
for r in range(N):
    for c in range(N):
        total_trees += len(trees_board[r][c])

print(total_trees)