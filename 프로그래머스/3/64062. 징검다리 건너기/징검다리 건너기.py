def solution(stones, k):
    left = 1
    right = 200_000_000  # 더 이상 건널 수 없을 때까지
    answer = 0
    
    def check(m):
        nonlocal k
        cnt = 0
        for i in range(len(stones)):
            if stones[i] < m:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                return True
        else:
            return False
    
    # 이분탐색
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        
        if check(mid): # mid명은 못 건넘
            right = mid - 1
        else: # 건널 수 있다면
            answer = mid
            left = mid + 1
    
    return answer