import sys
input = lambda: sys.stdin.readline().rstrip()

N, r, c = map(int, input().split())

def z(N, r, c, cnt):
    if N == 0:
        print(cnt)
        return
    stn = 2**(N-1)
    if r < stn and c < stn:
        z(N-1, r, c, cnt)
    elif r < stn and c >= stn:
        z(N-1, r, c-stn, cnt+stn**2)
    elif r >= stn and c < stn:
        z(N-1, r-stn, c, cnt+(stn**2)*2)
    elif r >= stn and c >= stn:
        z(N-1, r-stn, c-stn, cnt+(stn**2)*3)
        
z(N, r, c, 0)