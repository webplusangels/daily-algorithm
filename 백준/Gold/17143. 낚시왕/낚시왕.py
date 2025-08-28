import sys
input = lambda: sys.stdin.readline().rstrip()

R, C, M = map(int, input().split())
board = [[-1]*C for _ in range(R)]
sharks = []
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = i
    sharks.append([[r-1, c-1], s, d, z])

dx, dy = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)
dir_change = {1: 2, 2: 1, 3: 4, 4: 3}
def shark_moves(now):
    new_board = [[-1]*C for _ in range(R)]
    for i in range(M):
        shark = sharks[i]
        if not shark[0]:
            continue
        
        # 2 * standard로 나눔
        # 나온 좌표는 현재 좌표와 방향에 맞게 더해 다시 재조정해야함
        speed, dir = shark[1], shark[2]
        standard, cur = R-1 if dir <= 2 else C-1, 0 if dir <= 2 else 1
        dist = speed % (2*standard) # 2*standard 크기로 전체 맵을 만들고
        if dir == 2 or dir == 3:
            res = (shark[0][cur] + dist) % (2*standard)
        else:
            res = (shark[0][cur] - dist) % (2*standard)
        if res == 0 or res >= standard+1:
            shark[2] = dir_change[dir]
            shark[0][cur] = (2*standard - res) % standard
        else:
            shark[0][cur] = res
        x, y = shark[0]
        # 만약 상어가 겹친다면
        possible = new_board[x][y]
        if possible != -1:
            if shark[3] > sharks[possible][3]:
                sharks[possible][0] = None
                shark[0] = [x, y]
                new_board[x][y] = i
            else:
                shark[0] = None
        else:
            shark[0] = [x, y]
            new_board[x][y] = i
    return new_board

caught = 0
for now in range(C):
    # print(*board, sep='\n')
    # print(*sharks, sep='\n')
    # print(f"{caught=} {now=}")
    for i in range(R):
        ex = board[i][now]
        if ex != -1:
            caught += sharks[ex][3]
            board[i][now] = -1
            sharks[ex][0] = None
            break
    board = shark_moves(now)

print(caught)
    