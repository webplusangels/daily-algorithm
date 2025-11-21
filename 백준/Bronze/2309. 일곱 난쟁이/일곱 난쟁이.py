from itertools import combinations
import sys

def solution(lst):
    for comb in combinations(lst, 7):
        if sum(comb) == 100:
            comb = list(comb)
            comb.sort()
            return comb

nanjangs = []
for _ in range(9):
    nanjangs.append(int(input()))
print(*solution(nanjangs))