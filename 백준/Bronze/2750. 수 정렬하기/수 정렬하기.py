import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ns = [int(input()) for _ in range(N)]

ns.sort()

for i in range(N):
    print(ns[i])