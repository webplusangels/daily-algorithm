import sys
input = lambda: sys.stdin.readline().rstrip()
board = []
s_list = []
y_list = []
for i in range(5):
    line = list(input())
    for j in range(5):
        if line[j] == 'S':
            s_list.append((i, j))
        else:
            y_list.append((i, j))
    board.append(line)

s_list = sorted(s_list, key=lambda t: t[0] + t[1])
y_list = sorted(y_list, key=lambda t: t[0] + t[1])

# 6보다 떨어져 있는지
def check(new, old):
    for o in old:
        dist = abs(new[0] - o[0]) + abs(new[1] - o[1])
        if dist > 6:
            return False
    return True

# 백트래킹 / 검사 부분으로 나눠서 작성
def func():
    cnt = 0
    for s_count in range(4, min(len(s_list)+1, 8)):
        l, final = [], []
        def s_l(w):
            if len(l) == s_count:
                y_l(0, l[:])
                return

            for i in range(w, len(s_list)):
                if not check(s_list[i], l):
                    continue
                l.append(s_list[i])
                s_l(i+1)
                l.pop()
        def y_l(w, l):
            nonlocal cnt
            if len(l) == 7:
                if bfs(l):
                    cnt += 1
                return

            for i in range(w, len(y_list)):
                if not check(y_list[i], l):
                    continue
                l.append(y_list[i])
                y_l(i+1, l)
                l.pop()
        def bfs(l):
            s = set(l)
            dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
            queue = [s.pop()]
            while queue:
                x, y = queue.pop()
                for n in range(4):
                    xx, yy = x + dx[n], y + dy[n]
                    if (xx, yy) in s:
                        s.remove((xx, yy))
                        queue.append((xx, yy))
            if s:
                return False
            return True

        s_l(0)
        
    print(cnt)
            

func()