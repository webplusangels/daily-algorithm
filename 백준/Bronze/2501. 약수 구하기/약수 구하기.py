N, K = map(int, input().split())

def solution(n, k):
    i = 1
    cnt = 0
    while i <= n and cnt < k:
        is_divided = not bool(n % i)
        if is_divided:
            cnt += 1
        if cnt == k:
            return i
         
        i += 1
    return 0

answer = solution(N, K)
print(answer)