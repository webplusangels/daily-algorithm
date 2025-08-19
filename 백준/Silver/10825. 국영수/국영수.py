import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = []
for _ in range(N):
    tmp = input().split()
    tmp[1:] = list(map(int, tmp[1:]))
    ns.append(tmp)

ns.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for n in ns:
    print(n[0])