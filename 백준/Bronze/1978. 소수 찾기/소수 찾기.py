import math

def solution(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if not n % i:
            return False
    else:
        return True
    
N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    if solution(num):
        cnt += 1

print(cnt)