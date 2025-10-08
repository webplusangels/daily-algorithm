from itertools import product
from collections import defaultdict

def solution(board, skill):
    # skill = [type, r1, c1, r2, c2, degree]
    # type = 1:적, 2:아군, r1-r2:c1-c2 = 범위, degree = 정도
    # 1 이상이 파괴되지 않은 상태
    
    N, M = len(board), len(board[0])
    changes = [[0]*M for _ in range(N)]
    is_enemy = {1: -1, 2: 1}
    
    # 누적 데미지
    for sk in skill:
        tp, r1, c1, r2, c2, degree = sk
        damage = degree*is_enemy[tp]
        
        changes[r1][c1] += damage
        
        if c2 + 1 < M:
            changes[r1][c2+1] -= damage
        
        if r2 + 1 < N:
            changes[r2+1][c1] -= damage

        if r2 + 1 < N and c2 + 1 < M:
            changes[r2+1][c2+1] += damage
        
    # changes -> 누적합
    for i in range(N):
        for j in range(1, M):
            changes[i][j] += changes[i][j-1] 
    
    for j in range(M):
        for i in range(1, N):
            changes[i][j] += changes[i-1][j]
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + changes[i][j] >= 1:
                answer += 1
    
    # print(*changes, sep='\n')
    return answer
            
    # print(*board, sep='\n')