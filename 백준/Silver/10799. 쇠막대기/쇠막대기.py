from sys import stdin
input = lambda: stdin.readline().rstrip()

string = input()
cnt = 0
stack = []

for i, s in enumerate(string):
    if s == ')':
        if string[i-1] == ')':
            stack.pop()
            cnt += 1
        else:
            stack.pop()
            cnt += len(stack)
    else:
        stack.append(s)

print(cnt)