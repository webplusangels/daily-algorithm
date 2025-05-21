from sys import stdin
input = lambda: stdin.readline().rstrip()

bracket_dict = {')': ('(', 2), ']': ('[', 3)}
stack = []
brackets = input()

for bracket in brackets:
    try:
        if bracket in bracket_dict.keys():
            temp = 0
            bkt_v = bracket_dict[bracket]
            while stack[-1] != bkt_v[0]:
                temp += stack.pop()
            stack.pop()
            if temp:
                stack.append(bkt_v[1]*temp)
            else:
                stack.append(bkt_v[1])
        else:
            stack.append(bracket)
    except (TypeError, IndexError):
        print(0)
        break
else:
    try:
        print(sum(stack))
    except (TypeError, IndexError):
        print(0)