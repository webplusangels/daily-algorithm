import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    pnt_a = 0
    pnt_b = 0
    A.sort()
    B.sort()

    while pnt_a != N:
        if pnt_b == M:
            cnt += pnt_b
            pnt_a += 1
            continue
        a, b = A[pnt_a], B[pnt_b]
        if a <= b:
            pnt_a += 1
            cnt += pnt_b
        else:
            pnt_b += 1

    print(cnt)