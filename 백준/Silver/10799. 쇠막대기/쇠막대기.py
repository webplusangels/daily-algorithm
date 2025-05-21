from sys import stdin
input = lambda: stdin.readline().rstrip()

string = input()
cnt = stick = 0
past = None

for char in string:
    if char == '(':
        stick += 1
    else:
        stick -= 1
        if past == ')':
            cnt += 1
        else: 
            cnt += stick
    past = char

print(cnt)