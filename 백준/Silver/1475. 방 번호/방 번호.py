import sys
input = sys.stdin.readline

# 방 번호
N = input().strip()

nums = {str(n):0 for n in range(10)}

for n in N:
    nums[n] += 1

nums['6'] = nums['9'] = (nums['6'] + nums['9'] + 1) // 2

print(max(nums.values()))