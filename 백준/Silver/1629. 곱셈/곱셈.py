import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())

def abc(A, B, C):
    if B == 1:
        return A % C
    val = abc(A, B//2, C)
    result = (val * val) % C
    if B % 2:
        return (result * A) % C
    return result

print(abc(A, B, C))