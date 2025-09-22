import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
while coins:
    coin = coins.pop()
    while coin <= K:
        k, K = divmod(K, coin)
        cnt += k
    if K == 0:
        print(cnt)        
        break