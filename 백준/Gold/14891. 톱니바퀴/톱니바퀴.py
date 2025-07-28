import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

wheels = []
for _ in range(4):
    wheel = deque(map(int, list(input())))
    wheels.append(wheel)

K = int(input())
rots = []
for _ in range(K):
    rot = list(map(int, input().split()))
    rots.append(rot)

# 3번째와 7번째
def connection():
    connected = []
    for i, wheel in enumerate(wheels):
        if i == 0:
            third = wheel[2]
            continue
        if third != wheel[6]:
            connected.append(True)
        else:
            connected.append(False)
        third = wheel[2]
    return connected

def rotated_wheel(t, conn):
    wheels[t[0]-1].rotate(t[1])
    # 왼쪽
    l_num, l_rot = t
    while l_num > 1:
        if conn[l_num-2] == False:
            break
        l_rot = -1 * l_rot
        wheels[l_num-2].rotate(l_rot)
        l_num -= 1
    # 오른쪽
    r_num, r_rot = t
    while r_num < 4:
        if conn[r_num-1] == False:
            break
        r_rot = -1 * r_rot
        wheels[r_num].rotate(r_rot)
        r_num += 1

for r in rots:
    con = connection()
    rotated_wheel(r, con)

point = wheels[0][0] * 1 + wheels[1][0] * 2 + wheels[2][0] * 4 + wheels[3][0] * 8
print(point)