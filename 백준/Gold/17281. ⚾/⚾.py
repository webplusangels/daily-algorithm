import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
inngs = [list(map(int, input().split())) for _ in range(N)]

playing = [False] * 9
lineup = [0] * 8
max_score = 0
memo = dict()

# 라인업, 이닝 -> 
def scored(o):
    cur = score = 0
    for i in range(N):
        outs = 0
        base1 = base2 = base3 = 0
        while outs < 3:
            result = inngs[i][o[cur]]
            if result == 0:
                outs += 1
            elif result == 4:
                score += base1 + base2 + base3 + 1
                base1 = base2 = base3 = 0
            elif result == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif result == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif result == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            cur = (cur+1) % 9
    return score

def func(w):
    global max_score
    if w == 8:
        final = lineup[:3] + [0] + lineup[3:]
        max_score = max(max_score, scored(final))
        return

    for j in range(1, 9):
        if not playing[j]:
            lineup[w] = j
            playing[j] = True
            func(w+1)
            lineup[w] = 0
            playing[j] = False

func(0)
print(max_score)