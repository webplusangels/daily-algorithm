import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
which = {}
for i in range(N):
    line = list(input())
    for j in range(M):
        if line[j] == 'B':
            which['B'] = (i, j)
            line[j] = '.'
        elif line[j] == 'R':
            which['R'] = (i, j)
            line[j] = '.'
        elif line[j] == 'O':
            which['O'] = (i, j)
    board.append(line)

# 빨강, 파랑, 구멍 모두 하나씩
# 최소값 찾는 거니까 BFS?
dq = deque([(which['R'], which['B'], 0)])
dir =[(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set([(which['R'], which['B'])])

def ball_move(coor, direction, bd):
    x, y = coor
    while True:
        xx, yy = x + direction[0], y + direction[1]
        if not (0 <= xx < N and 0 <= yy < M):
            return (x, y)

        what = bd[xx][yy]
        if what == '.':
            x, y = xx, yy
        elif what == 'O':
            return 'holed'
        else:
            return (x, y)
        
def tilt(r_coor, b_coor, direction):
    bd = [board[i][:] for i in range(N)]
    rx, ry = r_coor
    bx, by = b_coor
    bd[rx][ry], bd[bx][by] = 'R', 'B'
    coor = [r_coor, b_coor]
    # 방향에서 가장 끝 쪽부터 파악하면 될 듯
    # 요소에 의해 정렬?
    coor.sort(key = lambda x: -sum(direction)*x[1-direction.index(0)])
    answer = [0, 0]
    for i in range(2):
        a = ball_move(coor[i], direction, bd)
        if coor[i] == b_coor:
            if a == 'holed':
                return 'fail'
            answer[1] = a
            bd[bx][by] = '.'
            bd[a[0]][a[1]] = 'B'
        else:
            answer[0] = a
            if a == 'holed':
                bd[rx][ry] = '.'
                continue
            bd[rx][ry] = '.'
            bd[a[0]][a[1]] = 'R'

    if answer[0] == 'holed':
        return 'success'

    return tuple(answer)
    
while dq:
    r_c, b_c, cnt = dq.popleft()
    if cnt >= 10:
        print(-1)
        break
    for n in range(4):
        new_bd = tilt(r_c, b_c, dir[n])
        if new_bd == "success":
            print(cnt+1)
            sys.exit(0)
        elif new_bd == "fail":
            continue
        else:
            if new_bd not in visited:
                dq.append((new_bd[0], new_bd[1], cnt+1))
                visited.add(new_bd)
else:
    print(-1)