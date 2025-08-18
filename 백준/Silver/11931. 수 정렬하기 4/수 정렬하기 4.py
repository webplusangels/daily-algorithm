import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = [int(input()) for _ in range(N)]

ns.sort(reverse=True)

print(*ns, sep='\n')