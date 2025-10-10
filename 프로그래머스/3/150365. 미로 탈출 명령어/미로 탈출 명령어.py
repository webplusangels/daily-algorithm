def solution(n, m, x, y, r, c, k):
    # n: 미로의 세로, m: 미로의 가로 ((1, 1)부터 시작)
    board = [['.']*m for _ in range(n)]
    
    # (1, 1)부터 시작하니까
    x, y = x-1, y-1
    r, c = r-1, c-1
    
    # 이동 딕셔너리
    moves = {
        'u': (-1, 0),
        'r': (0, 1),
        'l': (0, -1),
        'd': (1, 0),
    }
    
    # 시작 지점과 이동 경로, 이동 횟수 - x,y -> r,c로 이동
    dq = [(x, y, '', 0)]
    
    # 거리를 계산해서 가지치기를 할까?
    def is_possible(x, y, cnt):
        distance = abs(r-x) + abs(c-y)
        if distance > k-cnt:
            return False
        if distance % 2 != (k-cnt) % 2:
            return False
        return True
    
    # k번 이동해야 함
    while dq:
        i, j, ms, cnt = dq.pop()
        if cnt == k and i == r and j == c:
            return ms
        for d in moves.keys():
            dx, dy = moves[d]
            xx, yy = i+dx, j+dy
            if not is_possible(xx, yy, cnt+1):
                continue
            if 0 <= xx < n and 0 <= yy < m and cnt+1 <= k:
                dq.append((xx, yy, ms + d, cnt+1))
    
    return 'impossible'