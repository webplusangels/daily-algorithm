import sys
input = sys.stdin.readline

result = 1

for num in range(3):
    tmp = int(input().strip())
    result *= tmp
    
ztn = [0] * 10

for s in str(result):
    ztn[int(s)] += 1
    
for n in ztn:
    print(n)