import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    tower = towers.pop()
    while stack and stack[-1][1] < tower:
        tmp = stack.pop()
        answer[tmp[0]] = N-i
        
    stack.append((N-i-1, tower))

print(*(answer))