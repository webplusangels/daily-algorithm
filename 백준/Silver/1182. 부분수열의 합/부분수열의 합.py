import sys
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())
Ns = list(map(int, input().split()))

cnt = 0

def func(w, sms):
    global cnt
    if w == N:
        if sms == S:
            cnt += 1
        return

    func(w+1, sms+Ns[w])
    func(w+1, sms)

func(0, 0)

if S == 0:
    print(cnt-1)
else:
    print(cnt)