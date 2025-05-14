import sys
input = sys.stdin.readline

n = int(input())
count = 1
stack = []
answer = []
possible = True

for _ in range(n):
    target_num = int(input())
    
    # pop과 push case를 분리
    while count <= target_num:
        stack.append(count)
        answer.append('+')
        count += 1
    
    if stack and stack[-1] == target_num:
        stack.pop()
        answer.append('-')
    else:
        possible = False
        break

if possible:
    for a in answer:
        print(a)
else:
    print('NO')