import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

nums = [1]*N # 누적 숫자
pointers = [-1]*N # 인덱스를 가리킴

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] and nums[i] < nums[j]+1:
            nums[i] = nums[j] + 1
            pointers[i] = j

ml = max(nums)
print(ml)

start = nums.index(ml)
l = []
while start != -1:
    l.append(A[start])
    start = pointers[start]

print(*reversed(l))