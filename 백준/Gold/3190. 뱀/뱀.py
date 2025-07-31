import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    which = tuple(map(lambda x: int(x)-1, input().split()))
    apples.add(which)
L = int(input())
Ls = {}
for _ in range(L):
    sn = input().split()
    Ls[int(sn[0])] = sn[1]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
dir_n = 1
snake = deque([(0, 0)])
def move(s, dn):
    x, y = s[0][0] + dx[dn], s[0][1] + dy[dn]
    if 0 <= x < N and 0 <= y < N:
        if (x, y) in s:
            return []
        if (x, y) in apples:
            apples.remove((x, y))
        else:
            s.pop()
        s.appendleft((x, y))
        return s
    else:
        return []

def turn(dir):
    global dir_n
    if dir == 'L':
        return (dir_n-1) % 4
    elif dir == 'D':
        return (dir_n+1) % 4

sec = 0
while snake:
    sec += 1
    if sec-1 in Ls.keys():
        dir_n = turn(Ls[sec-1])
    snake = move(snake, dir_n)
print(sec)