from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
MAX_POS = 100000

# dist 배열: -1은 미방문, 그 외는 해당 위치까지의 최소 시간
dist = [-1] * (MAX_POS + 1)
q = deque()

# 시작점 초기화
q.append(N)
dist[N] = 0

while q:
    curr_pos = q.popleft()

    if curr_pos == K:
        break # 목표 도달

    # 1. 순간이동 (0초 소요)
    next_pos = curr_pos * 2
    if 0 <= next_pos <= MAX_POS and dist[next_pos] == -1: # 아직 방문 안 했다면
        dist[next_pos] = dist[curr_pos] # 시간 그대로
        q.appendleft(next_pos) # 우선순위가 높으므로 앞에 추가
    
    # 2. 걷기 (1초 소요)
    for next_pos in (curr_pos - 1, curr_pos + 1): # 순서 상관 없음
        if 0 <= next_pos <= MAX_POS and dist[next_pos] == -1: # 아직 방문 안 했다면
            dist[next_pos] = dist[curr_pos] + 1 # 시간 + 1
            q.append(next_pos) # 우선순위가 낮으므로 뒤에 추가

print(dist[K])