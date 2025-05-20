from sys import stdin
from collections import deque
import ast
input = lambda: stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    p = input()
    n = int(input())
    x_list = deque(ast.literal_eval(input()))
    r_flag = False
    
    for cmd in p:
        if cmd == 'R':
            r_flag = not r_flag
        else:
            if x_list:
                if r_flag:
                    x_list.pop()
                else:
                    x_list.popleft()
            else:
                print("error")
                break
    else:
        if r_flag:
            x_list.reverse()
        print(f"[{','.join(map(str, x_list))}]")