from collections import deque

def solution(m, n, board):
    # 4개가 붙어있는지 확인하기
    def check(board):
        nonlocal m, n
        to_pop = set()
        to_check = [(1, 0), (0, 1), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char == ' ':
                    continue
                cnt = set([(i, j)])
                flag = False
                for c in to_check:
                    x, y = i+c[0], j+c[1]
                    if 0 <= x < m and 0 <= y < n and board[x][y] == char:
                        cnt.add((x, y))
                    else:
                        flag = True
                        break
                if not flag:
                    to_pop.update(cnt)
        
        return to_pop

    # 이동하기
    def move(board, to_pop):
        nonlocal n, m
        new_board = [[' ']*n for _ in range(m)] 
        for j in range(n):
            cnt = m-1
            for i in range(m-1, -1, -1):
                if (i, j) in to_pop:
                    continue
                new_board[cnt][j] = board[i][j]
                cnt -= 1
                
        return new_board
    
    answer = 0
    
    while True:
        to_pop = check(board)
        tmp = len(to_pop)
        if not tmp:
            break
        answer += tmp
        board = move(board, to_pop)
        
    return answer
    