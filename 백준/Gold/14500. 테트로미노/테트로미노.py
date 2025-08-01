import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
get_ints = lambda: map(int, input().split())

N, M = get_ints()
board = []
for i in range(N):
    line = list(get_ints())
    board.append(line)

bases = [
    ((0, 0), (0, 1), (0, 2), (0, 3)), # 회전 한 번만, 뒤집기 X
    ((0, 0), (1, 0), (2, 0), (2, 1)), 
    ((0, 0), (1, 0), (0, 1), (1, 1)), # 회전, 뒤집기 X
    ((0, 0), (1, 0), (1, 1), (2, 1)), 
    ((0, 0), (1, 1), (0, 1), (0, 2))
]

def rotate(shape):
    return tuple(sorted([(s[1], -s[0]) for s in shape]))

def flip(shape):
    return tuple(sorted([(-s[0], s[1]) for s in shape]))

all_shapes = set()
for base_shape in bases:
    shape = base_shape
    for _ in range(4):
        all_shapes.add(shape)
        shape = rotate(shape)
    
    shape = flip(base_shape)
    for _ in range(4):
        all_shapes.add(shape)
        shape = rotate(shape)

max_val = 0
for r in range(N):
    for c in range(M):
        for shape in all_shapes:
            current_sum = 0
            is_valid = True
            for dr, dc in shape:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < M):
                    is_valid = False
                    break
                current_sum += board[nr][nc]
            
            if is_valid:
                max_val = max(max_val, current_sum)

print(max_val)