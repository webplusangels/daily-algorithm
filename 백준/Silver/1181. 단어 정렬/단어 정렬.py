import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = list(set([input() for _ in range(N)]))

ns.sort(key=lambda x: (len(x), x))
print(*ns, sep='\n')