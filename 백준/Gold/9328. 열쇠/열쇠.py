import sys
from collections import deque, defaultdict
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

for _ in range(T):
    h, w = map(int, input().split())
    which = defaultdict(set)
    board = []
    # 위치 기록
    for n in range(h):
        line = list(input())
        for i, char in enumerate(line):
            if n == 0 or n == h-1 or i == 0 or i == w-1:
                if char != '*':
                    which['edge'].add((n, i))
                if char.islower():
                    which["keys"].add(char)
                    line[i] = '.'
            if char.isupper():
                which[char].add((n, i))
        board.append(line)
    keys = set(input())
    if keys != {'0'}:
        which['keys'].update(keys)
    
    # 열쇠로 문 다 열기
    for key in which['keys']:
        # print(key)
        for kx, ky in which[key.upper()]:
            board[kx][ky] = '.'
        which.pop(key.upper())

    # 탐색 -> edge에서부터
    vis = [[False] * w for _ in range(h)]
    edges = list(which['edge'])
    for node in edges:
        nx, ny = node
        if board[nx][ny].isupper():
            which['edge'].remove(node)
        else:
            if board[nx][ny] == '$':
                which['$'].add((nx, ny))
            vis[nx][ny] = True
        # print(f'{which["edge"]=}')
    # print(which)
    dq = deque(which['edge'])
            
    while dq:
        # print(f"{dq=}")
        x, y = dq.popleft()
        if board[x][y].isalpha():
            door = board[x][y].upper()
            board[x][y] = '.'
            for wx, wy in which[door]:
                board[wx][wy] = '.'
                if wx == 0 or wx == h-1 or wy == 0 or wy == w-1:
                    dq.append((wx, wy))
                    vis[wx][wy] = True
                else:
                    for n in range(4):
                        xx, yy = dx[n] + wx, dy[n] + wy
                        if 0 <= xx < h and 0 <= yy < w and vis[xx][yy]:
                            dq.append((wx, wy))
                            vis[wx][wy] = True
                            break
                    
        for n in range(4):
            xx, yy = dx[n] + x, dy[n] + y
            if 0 <= xx < h and 0 <= yy < w and board[xx][yy] != '*' and not board[xx][yy].isupper() and not vis[xx][yy]:
                if board[xx][yy] == '$':
                    which['$'].add((xx, yy))
                vis[xx][yy] = True
                dq.append((xx, yy))
        # print(*board, sep="\n")
        # print(*vis, sep="\n")
        # print(which['$'])
    print(len(which['$']))
