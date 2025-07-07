import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

visited = [False] * (N+1)
sn = []

def nnm(set_num):
    if len(set_num) == M:
        print(*set_num)
        return

    for i in range(N):
        if not visited[i]:
            set_num.append(i+1)
            visited[i] = True
            nnm(set_num)
            set_num.pop()
            visited[i] = False

nnm(sn)