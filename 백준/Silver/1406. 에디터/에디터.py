import sys
input = sys.stdin.readline

input_str = input().strip()
M = int(input().strip())

left_stack = list(input_str)
right_stack = []

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if not left_stack:
            continue
        s = left_stack.pop()
        right_stack.append(s)
    elif cmd[0] == 'D':
        if not right_stack:
            continue
        s = right_stack.pop()
        left_stack.append(s)
    elif cmd[0] == 'B':
        if not left_stack:
            continue
        s = left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[1])
    
answer = left_stack + right_stack[::-1]
print(''.join(answer))