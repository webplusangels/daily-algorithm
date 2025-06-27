import sys
input = lambda: sys.stdin.readline().rstrip()

def hanoi(a, b, n):
    if n == 1:
        print(a, b) # count
        return

    hanoi(a, 6-a-b, n-1)
    print(a, b)
    hanoi(6-a-b, b, n-1)

N = int(input())

if N == 1:
    print(1)
else:
    print(2**N - 1)
hanoi(1, 3, N)