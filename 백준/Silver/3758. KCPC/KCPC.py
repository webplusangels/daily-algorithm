import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split()) # 팀의 개수, 문제의 개수, 팀 ID, 로그 엔트리 개수
    logs = [list(map(int, input().split())) for _ in range(m)] # 팀 ID, 문제 번호, 점수

    # 팀, 문제
    scoreboard = {(i, j): 0 for i in range(n) for j in range(k)}
    send = {i: 0 for i in range(n)}
    last = {i: 0 for i in range(n)}
    
    for e, log in enumerate(logs):
        i, j, s = log

        scoreboard[(i-1, j-1)] = max(scoreboard[(i-1, j-1)], s)
        send[i-1] += 1
        last[i-1] = e

    final_score = []
    for x in range(n):
        score = 0
        for y in range(k):
            score += scoreboard[(x, y)]
        final_score.append((x, score, send[x], last[x]))

    final_score.sort(key=lambda x: (-x[1], x[2], x[3]))

    for i in range(n):
        if final_score[i][0] == t-1:
            print(i+1)
            break