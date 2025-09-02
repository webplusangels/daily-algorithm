import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = []
    robot = None
    to_clean = []
    for i in range(h):
        tmp = list(input())
        for j in range(w):
            if not robot and tmp[j] == 'o':
                robot = (i, j)
            elif tmp[j] == '*':
                to_clean.append((i, j))
        board.append(tmp)

    l = len(to_clean) + 1
    moves = [[0]*l for _ in range(l)]

    def bfs(c_1, c_2):
        if moves[c_1][c_2]:
            return moves[c_1][c_2]
        c1, c2 = to_clean[c_1], to_clean[c_2]
        dq = deque([(c1[0], c1[1], 0)])
        vis = set()
        while dq:
            x, y, cnt = dq.popleft()
            for n in range(4):
                xx, yy = x+dx[n], y+dy[n]
                cc = (xx, yy)
                if xx < 0 or xx >= h or yy < 0 or yy >= w or cc in vis:
                    continue
                vis.add(cc)
                if board[xx][yy] == 'x':
                    continue
                if cc == c2:
                    moves[c_1][c_2] = cnt+1
                    moves[c_2][c_1] = cnt+1
                    return cnt+1
                dq.append((xx, yy, cnt+1))
        else:
            return -1

    to_clean = [robot] + to_clean
    cleaned = []
    flag = False
    for i in range(l):
        for j in range(i+1, l):
            dist = bfs(i, j)
            if dist == -1:
                flag = True
                break
        if flag:
            break

    if flag:
        print(-1)
        continue

    dp = [[float('inf')]*l for _ in range(1 << l)]
    dp[1][0] = 0

    for mask in range(1, 1 << l):
        for cur in range(l):
            if dp[mask][cur] == float('inf'):
                continue

            for nex in range(l):
                if not (mask & (1 << nex)):
                    nex_mask = mask | (1 << nex)
                    new = dp[mask][cur] + moves[cur][nex]

                    dp[nex_mask][nex] = min(dp[nex_mask][nex], new)

    final = (1 << l) - 1
    answer = min(dp[final])
    print(answer)
                    