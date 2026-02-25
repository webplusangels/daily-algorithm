import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = list(map(int, input().split()))
heaplist = [(n, i+1) for i, n in enumerate(ns)]
heapdict = {i+1: n for i, n in enumerate(ns)}
heapq.heapify(heaplist)

# dict로 현재 값을 저장 & heappush -> heappop -> dict 서치 -> 다르면 다시 뽑기
M = int(input())
for _ in range(M):
    nums = list(map(int, input().split()))
    if nums[0] == 2:
        while True:
            num, idx = heapq.heappop(heaplist)
            if heapdict[idx] == num:
                print(idx)
                heapq.heappush(heaplist, (num, idx))
                break
        
    elif nums[0] == 1:
        i, v = nums[1:]
        heapdict[i] = v
        heapq.heappush(heaplist, (v, i))