import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque(range(1, N + 1))
answer = []

while queue:
    for _ in range(K - 1):
        if queue:
            queue.append(queue.popleft())
    if queue:
        answer.append((queue.popleft()))

print('<', ', '.join(map(str, answer)), '>', sep='')