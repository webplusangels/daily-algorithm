import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
string = input()

strs = string*N
print(''.join(strs))