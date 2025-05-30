from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(l, now, target):
    if now == target:
        return 0
    else:
        dq = deque([(now[0], now[1], 0)])
        visited = [[False for _ in range(l)] for _ in range(l)]
        # 시작점도 방문 처리 해주기
        visited[now[0]][now[1]] = True
        while dq:
            cur_x, cur_y, cnt = dq.popleft()
            for i in range(8):
                xx = cur_x + dx[i]
                yy = cur_y + dy[i]
                if 0 <= xx < l and 0 <= yy < l and not visited[xx][yy]:
                    if (xx, yy) == target:
                        return cnt+1
                    dq.append((xx, yy, cnt+1))
                    visited[xx][yy] = True
                    
# 테스트 케이스
T = int(input())

for _ in range(T):
    l = int(input())
    knt_now = tuple(map(int, input().split()))
    knt_target = tuple(map(int, input().split()))

    print(bfs(l, knt_now, knt_target))