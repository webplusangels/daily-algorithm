def solution(queue1, queue2):
    total = queue1 + queue2
    length = len(queue1)*2
    window_sum = sum(queue1)
    all_sum = window_sum + sum(queue2)
    num = all_sum // 2
    
    # 움직이며 목표치와 비교
    start, end = 0, length // 2
    cnt = 0
    while end < length:
        if window_sum == num:
            return cnt
        
        if window_sum < num:
            window_sum += total[end]
            end += 1
        elif window_sum > num:
            window_sum -= total[start]
            start += 1
        cnt += 1
    else:
        return -1