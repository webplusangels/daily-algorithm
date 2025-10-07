import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parents = [x for x in range(n)]

def find(x):
    parent_x = parents[x]
    
    if parent_x == x:
        return x
        
    parents[x] = find(parent_x)
    return parents[x]

for i in range(m):
    x, y = map(int, input().split())

    x_root = find(x)
    y_root = find(y)

    if x_root > y_root:
        parents[x_root] = y_root
    elif x_root < y_root:
        parents[y_root] = x_root
    else:
        print(i+1)
        break
else:
    print(0)
    
    # print(f"{x=} {x_root=}, {y=} {y_root=}")
    # print(parents)