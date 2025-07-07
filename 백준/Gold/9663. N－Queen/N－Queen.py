import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
col = [False] * N
col_1 = [False] * (2*N - 1) # 대각
col_2 = [False] * (2*N - 1) # 대각
cnt = 0

def queen(n):
    global cnt
    if n == N:
        cnt += 1
        return

    for i in range(N):
        if not col[i] and not col_1[n+i] and not col_2[N-1-n+i]:
            col[i] = True
            col_1[n+i] = True
            col_2[N-1-n+i] = True
            queen(n+1)
            col[i] = False
            col_1[n+i] = False
            col_2[N-1-n+i] = False


queen(0)
print(cnt)