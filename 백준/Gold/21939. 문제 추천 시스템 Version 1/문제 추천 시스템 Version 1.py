import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 최대힙, 최소힙, 딕셔너리
max_heap, min_heap, check_dict = [], [], {}
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))
    check_dict[P] = L

M = int(input())
cmds = [input().split() for _ in range(M)]

for cmd in cmds:
    c = cmd[0]
    if c == 'recommend':
        if cmd[1] == '1':
            while not check_dict.get(-max_heap[0][1]) or check_dict[-max_heap[0][1]] != -max_heap[0][0]:
                heapq.heappop(max_heap)
            L, P = max_heap[0]
            print(-P)
        elif cmd[1] == '-1':
            while not check_dict.get(min_heap[0][1]) or check_dict[min_heap[0][1]] != min_heap[0][0]:
                heapq.heappop(min_heap)
            L, P = min_heap[0]
            print(P)
    elif c == 'add':
        P, L = map(int, [cmd[1], cmd[2]])
        heapq.heappush(max_heap, (-L, -P))
        heapq.heappush(min_heap, (L, P))
        check_dict[P] = L
    elif c == 'solved':
        P = int(cmd[1])
        check_dict.pop(P)