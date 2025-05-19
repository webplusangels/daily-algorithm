import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
deq = deque([])

def queue_cmd(cmd: list[str]) -> None:
    if cmd[0] == 'push':
        deq.append(cmd[1])
    elif cmd[0] == 'pop':
        num = -1
        if deq:
            num = deq.popleft()
        print(num)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)

for _ in range(N):
    cmd = input().split()
    queue_cmd(cmd)
