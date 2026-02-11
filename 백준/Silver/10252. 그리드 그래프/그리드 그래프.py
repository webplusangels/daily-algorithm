import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

def func(r, c):
    if not r % 2:
        for i in range(r):
            if not i % 2:
                for j in range(c):
                    print(f"({i},{j})")
            else:
                for j in range(c-1, -1, -1):
                    print(f"({i},{j})")
    elif not c % 2:
        for j in range(c):
            if not j % 2:
                for i in range(r):
                    print(f"({i},{j})")
            else:
                for i in range(r-1, -1, -1):
                    print(f"({i},{j})")
    else:
        print("(0,0)")
        for i in range(r):
            if not i % 2:
                for j in range(1, c):
                    print(f"({i},{j})")
            else:
                for j in range(c-1, 0, -1):
                    print(f"({i},{j})")
        for i in range(r-1, 0, -1):
            print(f"({i},0)")
        
for _ in range(T):
    R, C = map(int, input().split())

    print(1)
    func(R, C)