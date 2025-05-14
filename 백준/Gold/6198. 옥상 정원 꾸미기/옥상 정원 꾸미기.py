import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = [0] * N
for i in range(N+1):
    if i == N:
        roof = float("inf")
    else:
        roof = int(input())
    while stack and stack[-1][1] <= roof:
        block = stack.pop()
        answer[block[0]] = i - block[0] - 1
    
    stack.append((i, roof))

print(sum(answer))