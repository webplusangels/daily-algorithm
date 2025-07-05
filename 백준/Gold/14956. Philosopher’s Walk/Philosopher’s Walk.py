import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

def philos(n, m):
    if n == 1:
        return (0, 0)

    new_n = n // 2
    k = m // (new_n)**2
    new_m = m % (new_n)**2
    
    x_, y_ = philos(new_n, new_m)
    if k == 0:
        # 90도 회전
        x_, y_ = y_, x_
        return (x_, y_)
    if k == 1:
        return (x_, y_+new_n)
    if k == 2:
        return (x_+new_n, y_+new_n)
    if k == 3:
        # x_와 y_의 범위는 (0 ~ new_n-1)
        # 최대값 - 변수 -> new_n - 1 - (x_, y_)
        x_, y_ = new_n - 1 - y_, new_n - 1 - x_
        return (x_+new_n, y_) 
    
print(*map(lambda x: x+1, philos(n, m-1)))