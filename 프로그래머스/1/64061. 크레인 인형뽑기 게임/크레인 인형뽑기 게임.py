def solution(board, moves):
    # moves의 순서대로 이동
    # x좌표를 1씩 늘려가면서 move-1을 확인
    # 0이 아니면 쌓이는 블록
    h = len(board)
    cnt = 0
    basket = []
    for move in moves:
        tmp = 0
        for i in range(h):
            if board[i][move-1]:
                tmp = board[i][move-1]
                board[i][move-1] = 0
                break
        if basket and basket[-1] == tmp: # basket에 인형이 있고, 마지막 인형이 같다면
            basket.pop()
            cnt += 2
        elif tmp != 0: # 인형을 집었다면
            basket.append(tmp)
            
    return cnt