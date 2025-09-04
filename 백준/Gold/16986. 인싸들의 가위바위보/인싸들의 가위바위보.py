import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
frnds = [list(map(int, input().split())) for _ in range(2)]

def winner(m):
    h1, h2 = m
    if h1 == h2:
        return 2
    else:
        if table[h1][h2] == 2:
            return 0
        else:
            return 1

win = [0, 0, 0]
pos = [0, 0, 0]
vis = [False]*N

answer = 0
def func(match):
    global answer
    if answer == 1 or win[1] >= K or win[2] >= K:
        return
    
    # w는 지우 턴의 개수, match는 i(인덱스)로 이루어진 길이가 2인 튜플 
    if win[0] == K:
        answer = 1
        return

    matches = []
    if 0 in match:
        for zz in range(N):
            if vis[zz]:
                continue
            # 승부: 인덱스 찾기
            z_i = match.index(0)
            n_i = 1 - z_i
            fr = match[n_i]
            # 손동작
            tmp = [-1, -1]
            tmp[z_i] = zz
            tmp[n_i] = frnds[fr-1][pos[fr]]-1
            winn = winner(tmp)
            if winn == 2:
                winn = n_i
            # 다음 매치
            # 승부는 계속된다
            vis[zz] = True
            pos[fr] += 1
            pos[0] += 1
            win[match[winn]] += 1
            next_match = [match[winn], 3-fr]
            func(next_match)
            vis[zz] = False
            pos[fr] -= 1
            pos[0] -= 1
            win[match[winn]] -= 1
    else:
        fr_1, fr_2 = match
        tmp = [frnds[fr_1-1][pos[fr_1]]-1, frnds[fr_2-1][pos[fr_2]]-1]
        winn = winner(tmp)
        if winn == 2:
            winn = match.index(2)
        pos[fr_1] += 1
        pos[fr_2] += 1
        win[match[winn]] += 1
        next_match = [match[winn], 0]
        func(next_match)
        pos[fr_1] -= 1
        pos[fr_2] -= 1
        win[match[winn]] -= 1

func([0, 1])
print(answer)