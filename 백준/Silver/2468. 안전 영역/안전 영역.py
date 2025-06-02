from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N = int(input())
square = []
min_num = float('inf')
max_num = float('-inf')

for _ in range(N):
    n_list = list(map(int, input().split()))
    square.append(n_list)
    for n in n_list:
        min_num = min(min_num, n)
        max_num = max(max_num, n)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num_area = 1

for n in range(min_num, max_num):
    filtered_square = [[True if num > n else False for num in line] for line in square]
    cnt = 0
    dq = deque([])
    for i in range(N):
        for j in range(N):
            if filtered_square[i][j]:
                dq.append((i, j))
                filtered_square[i][j] = False
                cnt += 1
                while dq:
                    x, y = dq.popleft()
                    for l in range(4):
                        xx = dx[l] + x
                        yy = dy[l] + y
                        if 0 <= xx < N and 0 <= yy < N and filtered_square[xx][yy]:
                            dq.append((xx, yy))
                            filtered_square[xx][yy] = False

    num_area = max(num_area, cnt)

print(num_area)