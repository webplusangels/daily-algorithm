import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

def cal_status(w):
    s = 0
    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                s += table[w[i]][w[j]]
    return s

whole = set([n for n in range(N)])
minn = float('inf')
vis = set()
def func(i, w):
    global minn
    if len(w) == N//2:
        if tuple(w) not in vis:
            ano_w = list(whole - set(w))
            answer = abs(cal_status(w) - cal_status(ano_w))
            vis.add(tuple(ano_w))
            minn = min(minn, answer)
        return

    for n in range(i, N):
        w.append(n)
        func(n+1, w)
        w.pop()
    
func(0, [])
print(minn)