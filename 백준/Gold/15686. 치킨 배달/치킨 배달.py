import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
which = {1: [], 2: []}
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            which[1].append((i, j))
        elif line[j] == 2:
            which[2].append((i, j))
    board.append(line)

# 치킨집 고르기
# 각각 거리 재기
# 최소값 업데이트
len_chk = len(which[2])
chkns = []
mn = float('inf')
def backtrack(w):
    global mn
    if len(chkns) == M:
        mn = min(mn, distance())
        return

    for i in range(w, len_chk):
        chkns.append(which[2][i])
        backtrack(i+1)
        chkns.pop()

def distance():
    dis = 0
    for p in which[1]:
        lst = []
        for chk in chkns:
            lst.append(abs(p[0] - chk[0]) + abs(p[1] - chk[1]))
        dis += min(lst)
    return dis

backtrack(0)
print(mn)