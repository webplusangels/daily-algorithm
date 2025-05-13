import sys
from collections import Counter
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

counter1 = Counter(str1)
counter2 = Counter(str2)

answer = (counter1 | counter2) - (counter1 & counter2)
print(sum(answer.values()))