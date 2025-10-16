import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [int(input()) for _ in range(N)]

neg = []
pos = []
ones = 0
for i in range(len(nums)):
    if nums[i] <= 0:
        neg.append(nums[i])
    elif nums[i] == 1:
        ones += 1
    elif nums[i] > 1:
        pos.append(nums[i])

acc = 0

def to_sum(l):
    sums = 0
    if not l:
        return 0
    
    for i in range((len(l)+1)//2):
        if 2*i+1 >= len(l):
            # print(l[2*i])
            sums += l[2*i]
        else:
            sums += l[2*i]*l[2*i+1]
        
    return sums

# 음수
neg.sort()
acc += to_sum(neg)

# 양수
pos.sort(reverse=True)
acc += to_sum(pos)

# 1
acc += ones

print(acc)