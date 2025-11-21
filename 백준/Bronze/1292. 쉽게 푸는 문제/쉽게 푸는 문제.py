def solution(s, e):
    cnt = 0
    num = 1
    arr = [0]
    for i in range(1, e+1):
        arr.append(num+arr[-1])
        cnt += 1
        if num == cnt:
            num += 1
            cnt = 0

    return arr[e] - arr[s-1]

s, e = map(int, input().split())
print(solution(s, e))