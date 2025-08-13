import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]

dirs = ((1, 0), (0, -1), (-1, 0), (0, 1))
points = set()

def move(ds, p):
    answer = []
    for d in ds:
        p = (p[0]+dirs[d][0], p[1]+dirs[d][1])
        answer.append(p)
    return answer

for i in range(len(curves)):
    x, y, d, g = curves[i]
    ps = [(x, y), (x+dirs[d][0], y+dirs[d][1])]
    
    ds = []
    for _ in range(g):
        if not ds:
            ds.append((d+1)%4)
        else:
            ds_rev = [(n+1)%4 for n in reversed(ds)]
            ds = ds_rev + ds
        ps = ps + move(ds, ps[-1])

    points.update(ps)

def check_square():
    points_l = list(points)
    cnt = 0
    for p in points_l:
        x, y = p
        com = {(x+1, y), (x, y+1), (x+1, y+1)}
        if com & points == com:
            cnt += 1
    return cnt

print(check_square())