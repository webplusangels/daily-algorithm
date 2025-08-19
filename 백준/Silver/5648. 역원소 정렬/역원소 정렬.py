import sys
input = lambda: sys.stdin.readline().rstrip()

tmp = input().split()
N = int(tmp[0])
ns = tmp[1:]

while len(ns) < N:
    tmp = input().split()
    ns.extend(tmp)

reversed_ns = sorted([int(n[::-1]) for n in ns])

print(*reversed_ns, sep='\n')
