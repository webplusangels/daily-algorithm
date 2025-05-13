import sys
input = sys.stdin.readline

num_cases = int(input().strip())

for _ in range(num_cases):
    input_str = input().strip()
    left_stack = []
    right_stack = []
    
    for s in input_str:
        if s == '-':
            if left_stack:
                left_stack.pop()
        elif s == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif s == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(s)
    
    answer = left_stack + right_stack[::-1]
    print(''.join(answer))
            