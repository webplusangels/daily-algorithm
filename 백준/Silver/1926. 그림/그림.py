from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
picture = []

for _ in range(n):
    temp = list(map(int, input().split()))
    picture.append(temp)

def bfs(picture: list[list[int]], n: int, m: int) -> list[int]:
    dq = deque()
    max_area = 0
    count = 0
    for i in range(n):
        for j in range(m):
            if picture[i][j]:
                area = 0
                dq.append((i, j))
                picture[i][j] = 0
                while dq:
                    i_, j_ = dq.popleft()
                    area += 1
                    if i_-1 >= 0 and picture[i_-1][j_]:
                        dq.append((i_-1, j_))
                        picture[i_-1][j_] = 0
                    if j_-1 >= 0 and picture[i_][j_-1]:
                        dq.append((i_, j_-1))
                        picture[i_][j_-1] = 0
                    if i_+1 < n and picture[i_+1][j_]:
                        dq.append((i_+1, j_))
                        picture[i_+1][j_] = 0
                    if j_+1 < m and picture[i_][j_+1]:
                        dq.append((i_, j_+1))
                        picture[i_][j_+1] = 0
                max_area = max(max_area, area)
                count += 1
                
    return [count, max_area]

count, max_area = bfs(picture, n, m)
print(count)
print(max_area)