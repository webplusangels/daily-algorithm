import sys
input = lambda: sys.stdin.readline().rstrip()

fib = [0]*91
fib[0], fib[1] = 0, 1

n = int(input())

for i in range(2, n+1):
    fib[i] = fib[i-2] + fib[i-1]

print(fib[n])