import sys
from bisect import bisect_right
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
line = list(map(int, input().split()))
if N == 1:
    print("권병장님, 중대장님이 찾으십니다")
    exit()

rng = list(map(int, input().split()))

p = 0
max_reach = line[0] + rng[0]
last_checked = 0

while True:
    if max_reach >= line[-1]:
        print("권병장님, 중대장님이 찾으십니다")
        break
    
    right = bisect_right(line, max_reach)
    
    best_reach = max_reach
    for i in range(last_checked + 1, right):
        potential = line[i] + (rng[i] if i < N-1 else 0)
        if potential > best_reach:
            best_reach = potential
    
    if best_reach == max_reach:
        print("엄마 나 전역 늦어질 것 같아")
        break
    
    last_checked = right - 1
    max_reach = best_reach