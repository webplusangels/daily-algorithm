from sys import stdin
input = lambda: stdin.readline().rstrip()

brackets = {'(': ')', '[': ']'}

while True:
    string = input()
    if string == '.':
        break
    stack = []
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' or s == ']':
            if stack:
                compared = stack.pop()
            else:
                print('no')
                break
            if brackets[compared] != s:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')