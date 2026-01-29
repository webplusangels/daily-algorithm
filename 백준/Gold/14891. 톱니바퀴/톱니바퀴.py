import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

chains = [deque(map(int, list(input()))) for _ in range(4)]
K = int(input())
spins = [list(map(int, input().split())) for _ in range(K)]

# 1번의 idx 2, 2번의 6/ 2번의 2, 3번의 6/ 3번의 2, 4번의 6
state = [chains[0][2] != chains[1][6], chains[1][2] != chains[2][6], chains[2][2] != chains[3][6]]


# 시계 1, 반시계 -1
for spin in spins:
    num, dir = spin
    chains[num-1].rotate(dir)
    # 1번을 돌리면 1 -> 0
    # 2번을 돌리면 0, 2 -> 0 1
    # 3번을 돌리면 1, 3 -> 1 2
    # 4번을 돌리면 3 -> 2

    if num == 1:
        if state[0]:
            chains[1].rotate(-dir)
            if state[1]:
                chains[2].rotate(dir)
                if state[2]:
                    chains[3].rotate(-dir)
    elif num == 2:
        if state[0]:
            chains[0].rotate(-dir)
        if state[1]:
            chains[2].rotate(-dir)
            if state[2]:
                chains[3].rotate(dir)
    elif num == 3:
        if state[1]:
            chains[1].rotate(-dir)
            if state[0]:
                chains[0].rotate(dir)
        if state[2]:
            chains[3].rotate(-dir)
    elif num == 4:
        if state[2]:
            chains[2].rotate(-dir)
            if state[1]:
                chains[1].rotate(dir)
                if state[0]:
                    chains[0].rotate(-dir)
    # state 확인
    state = [chains[0][2] != chains[1][6], chains[1][2] != chains[2][6], chains[2][2] != chains[3][6]]

score = 0
for i, chain in enumerate(chains):
    score += chain[0]*(2**i)

print(score)