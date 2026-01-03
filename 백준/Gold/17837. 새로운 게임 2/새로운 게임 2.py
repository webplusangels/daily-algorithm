import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [list(map(int, input().split())) for _ in range(K)]
dirs = list(map(lambda x: [x[0]-1, x[1]-1, x[2]], dirs))
stacked = [[[] for _ in range(N)] for _ in range(N)]
dir_mean = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

# 말이 4개 이상 쌓이면 게임 종료
# 흰색(0): 그대로 이동
# 빨간색(1): 쌓여있던 말의 순서를 뒤집어서 이동
# 파란색(2) 혹은 장외: 말의 이동 방향을 반대로하고 한 칸 이동

for i, d in enumerate(dirs):
    stacked[d[0]][d[1]].append(i)

def move(i):
    x, y, dir = dirs[i]
    xx, yy = x + dir_mean[dir][0], y + dir_mean[dir][1]

    # 파란색, 장외
    if xx < 0 or yy < 0 or xx >= N or yy >= N or board[xx][yy] == 2:
        if dir % 2:
            dir += 1
        else:
            dir -= 1
        dirs[i][2] = dir
        xx, yy = x + dir_mean[dir][0], y + dir_mean[dir][1]
        
        if xx < 0 or yy < 0 or xx >= N or yy >= N or board[xx][yy] == 2:
            return False

    idx = stacked[x][y].index(i)
    to_move = stacked[x][y][idx:]
    
    stacked[x][y] = stacked[x][y][:idx]

    # 빨간색
    if board[xx][yy] == 1:
        to_move.reverse()

    stacked[xx][yy].extend(to_move)

    for horse_idx in to_move:
        dirs[horse_idx][0] = xx
        dirs[horse_idx][1] = yy

    if len(stacked[xx][yy]) >= 4:
        return True
        
    return False

i = 1
while True:
    if i > 1000:
        print(-1)
        break
        
    for x in range(K):
        result = move(x)    
        if result:
            print(i)
            sys.exit(0)
    
    i += 1