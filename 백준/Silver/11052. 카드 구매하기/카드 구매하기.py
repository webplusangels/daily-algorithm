import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
P = list(map(int, input().split()))

cards = [0]+P

for i in range(2, N+1):
    for j in range(1, i):
        cards[i] = max(cards[i-j]+cards[j], cards[i])

print(cards[N])