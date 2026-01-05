import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M, T = map(int, input().split())
disks = [deque(map(int, input().split())) for _ in range(N)]
xdk = [list(map(int, input().split())) for _ in range(T)]

sums = sum(sum(l) for l in disks)
numbers = N*M

# x의 배수인 원판을 d(0, 1)로 k칸 회전
# 인접하면서 같은 수를 지우자 (-1로 표기)
# 인접 수가 없으면 모든 수 평균을 기준으로 큰 수는 1을 빼고 작은 수는 1을 더함
def rotate_disk(x, d, k):
    for i in range(N//x):
        disks[(i+1)*x - 1].rotate(-1*k if d else 1*k)

def check():
    to_move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[False] * M for _ in range(N)] # 방문 체크용    
    dq = deque()
    cnt = nm = 0
    
    for i in range(N):
        for j in range(M):
            if disks[i][j] == -1 or visited[i][j]:
                continue
                
            dq = deque([(i, j)])
            visited[i][j] = True
            to_del = [(i, j)]
            target = disks[i][j]
            
            while dq:
                ii, jj = dq.popleft()
                for di, dj in to_move:
                    ni = ii + di
                    nj = (jj + dj) % M

                    if 0 <= ni < N and not visited[ni][nj] and target == disks[ni][nj]:
                        visited[ni][nj] = True
                        dq.append((ni, nj))
                        to_del.append((ni, nj))

            if len(to_del) >= 2:
                for ii, jj in to_del:
                    disks[ii][jj] = -1
                    cnt += target
                    nm += 1

    return cnt, nm

for x, d, k in xdk:
    rotate_disk(x, d, k)
    deleted_sum, num = check()
    sums -= deleted_sum
    numbers -= num
    
    if deleted_sum == 0:
        if numbers == 0:
            continue
        
        avg = sums / numbers
        for i in range(N):
            for j in range(M):
                if disks[i][j] == -1:
                    continue

                if disks[i][j] > avg:
                    disks[i][j] -= 1
                    sums -= 1
                elif disks[i][j] < avg:
                    disks[i][j] += 1
                    sums += 1

print(sums)