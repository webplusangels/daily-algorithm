import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().strip())

def strfry(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

for _ in range(N):
    s1, s2 = input().split()
    if strfry(s1, s2):
        print("Possible")
    else:
        print("Impossible")