from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

# area의 크기
N = int(input())

area = []
for _ in range(N):
    line = list(map(int, input().split()))
    area.append(line)

visited = [[0 for _ in range(N)] for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
num = 0

dq = deque()
to_visit = set()

# 데크에 저장
for i in range(N):
    for j in range(N):
        if area[i][j] == 1 and not visited[i][j]:
            num += 1
            dq.append((i, j))
            visited[i][j] = num
            while dq:
                x, y = dq.popleft()
                for n in range(4):
                    xx, yy = dx[n] + x, dy[n] + y
                    if 0 <= xx < N and 0 <= yy < N:
                        if not visited[xx][yy] and area[xx][yy] == 1:
                            dq.append((xx, yy))
                            visited[xx][yy] = num
                        if area[xx][yy] == 0:
                            to_visit.add((x, y, 0, num))

to_visit_dq = deque(to_visit)
cnt_map = [[0 for _ in range(N)] for _ in range(N)]

# (x, y, 회차, 몇 번 섬인지 -> 같은 섬이 아니면서 방문한 상태이면 그 때 회차를 출력)
# 순회하는 dq에는 무엇을 넣어야 할까? -> area가 0일 것, visited가 0이거나 본인의 섬과 다를 것, 

while to_visit_dq:
    x, y, cnt, i_num = to_visit_dq.popleft()
    for n in range(4):
        xx, yy = dx[n] + x, dy[n] + y
        if 0 <= xx < N and 0 <= yy < N and \
            area[xx][yy] == 0:
            if visited[xx][yy] == 0:
                to_visit_dq.append((xx, yy, cnt+1, i_num))
                visited[xx][yy] = i_num
                cnt_map[xx][yy] = cnt+1
            elif visited[xx][yy] != i_num:
                print(cnt_map[xx][yy] + cnt)                
                exit()