from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
                    
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        m, n = map(int, input().split())
        farm[n][m] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            K_dq = deque()
            if farm[i][j] == 1:
                K_dq.append((i, j))
                farm[i][j] = 0
                cnt += 1
                
                while K_dq:
                    x, y = K_dq.popleft()
                    for cur in range(4):
                        kx = x + dx[cur]
                        ky = y + dy[cur]
                        if 0 <= kx < N and 0 <= ky < M and farm[kx][ky] == 1:
                            K_dq.append((kx, ky))
                            farm[kx][ky] = 0

    print(cnt)