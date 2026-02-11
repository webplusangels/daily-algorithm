import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
coins = [list(input()) for _ in range(N)]

def count_tail(c):
    result = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if c[i][j] == 'T':
                cnt += 1

        result += min(cnt, N-cnt)

    return result

mn = float('inf')

def flip(idx):
    for j in range(N):
        coins[idx][j] = 'T' if coins[idx][j] == 'H' else 'H'

def func(n):
    global mn
    
    if n == N:
        mn = min(mn, count_tail(coins))
        return
    
    func(n+1)
    flip(n)
    func(n+1)
    flip(n)
    
        
func(0)
print(mn)