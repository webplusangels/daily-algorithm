import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
cards = deque([i for i in range(1, N+1) if i % 2 != 1])
count = N % 2
card = 1

while cards:
    card = cards.popleft()
    if count % 2:
        cards.append(card)
    count += 1
    
print(card)