import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
students = defaultdict(int)

for _ in range(N):
    student = input().strip()
    students[student] += 1
    
count = 0
for v in students.values():
    count += (v + K-1) // K

print(count)