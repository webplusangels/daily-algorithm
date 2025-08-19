import sys
input = lambda: sys.stdin.readline().rstrip()

string = input()

def func(s):
    length = len(s)
    l = []
    for i in range(1, length+1):
        l.append(s[-i:])

    return l

str_l = func(string)
str_l.sort()

print(*str_l, sep='\n')