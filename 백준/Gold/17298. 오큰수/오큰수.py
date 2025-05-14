import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
stack = []
answer = [-1] * N

for i in range(N):
    while stack and stack[-1][1] < A_list[i]:
        NGE = stack.pop()
        answer[NGE[0]] = A_list[i]
        
    stack.append((i, A_list[i]))
    
print(*answer)