import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
K_size = []
Ks = []

for _ in range(K):
    size = tuple(map(int, input().split()))
    area = []
    for _ in range(size[0]):
        line = list(map(int, input().split()))
        area.append(line)
    Ks.append(area)
    K_size.append(size)

board = [[0] * M for _ in range(N)]

def loop(x, y):
    for j in range(y + 1):
        for i in range(x + 1):
            if attach(sticker, sticker_size, i, j):
                return True
    return False

# 붙이기 여부를 확인하고 붙일 수 있으면 붙이고 True 반환
def attach(s, s_size, i, j):
    for x in range(s_size[0]):
        for y in range(s_size[1]):
            if s[x][y]:
                if board[j+x][i+y]:
                    return False
                    
    for x in range(s_size[0]):
        for y in range(s_size[1]):
            if s[x][y]:
                board[j+x][i+y] = 1                
    return True

def rotate(s, s_size):
    rotated = [[s[s_size[0]-1-j][i] for j in range(s_size[0])] for i in range(s_size[1])]
    return rotated

for w in range(K):
    sticker = Ks[w]
    sticker_size = K_size[w]

    for n in range(4):
        loop_x = M - sticker_size[1]
        loop_y = N - sticker_size[0]
        if loop(loop_x, loop_y):
            break
        sticker = rotate(sticker, sticker_size)
        sticker_size = (sticker_size[1], sticker_size[0])

# 면적 계산
# print(*board, sep='\n')
cnt = 0
for line in board:
    cnt += line.count(1)
# 출력
print(cnt)
