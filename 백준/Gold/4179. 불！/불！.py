from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

R, C = map(int, input().split())
maze = []
F_deq = deque()
J_deq = deque()

F_maze = [[0 for _ in range(C)] for _ in range(R)]
J_maze = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    line = list(input())
    maze.append(line)

    # J와 F의 위치
    for c, s in enumerate(line):
        if s == 'J':
            J_deq.append((r, c))
            J_maze[r][c] = 1
        if s == 'F':
            F_deq.append((r, c))
            F_maze[r][c] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while F_deq:
    f_i, f_j = F_deq.popleft()
    for i in range(4):
        fr, fc = f_i+dr[i], f_j+dc[i]
        if 0 <= fr < R and 0 <= fc < C and maze[fr][fc] != '#' and F_maze[fr][fc] == 0:
            F_maze[fr][fc] = F_maze[f_i][f_j] + 1
            F_deq.append((fr, fc))

escape = 0
while J_deq:
    j_i, j_j = J_deq.popleft()

    # 탈출 조건
    if j_i == 0 or j_i == R-1 or j_j == 0 or j_j == C-1:
        escape = J_maze[j_i][j_j]
        break
        
    for i in range(4):
        jr, jc = j_i+dr[i], j_j+dc[i]
        if 0 <= jr < R and 0 <= jc < C and maze[jr][jc] != "#" and J_maze[jr][jc] == 0:
            if F_maze[jr][jc] > J_maze[j_i][j_j] + 1 or F_maze[jr][jc] == 0:
                J_maze[jr][jc] = J_maze[j_i][j_j] + 1
                J_deq.append((jr, jc))

if escape:
    print(escape)
else:
    print("IMPOSSIBLE")