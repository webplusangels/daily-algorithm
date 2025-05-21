from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
cnt = 0

for _ in range(N):
    string = input()
    stack = []
    for char in string:
        if stack:
            if stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        else:
            stack.append(char)
    if not stack:
        cnt += 1
        
print(cnt)