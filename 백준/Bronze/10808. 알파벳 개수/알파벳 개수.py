import sys
input = sys.stdin.readline

# 단어 S
S = input().strip()

# 알파벳 딕셔너리
alp = {alp:0 for alp in 'abcdefghijklmnopqrstuvwxyz'}

for s in S:
    alp[s] += 1

print(*alp.values())