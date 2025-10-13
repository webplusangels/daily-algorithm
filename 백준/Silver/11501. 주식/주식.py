import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    profit = 0
    m = 0
    
    for i in range(N-1, -1, -1):
        if stocks[i] > m:
            m = stocks[i]
        else:
            profit += m - stocks[i]

    print(profit)