import sys

input = lambda: sys.stdin.readline().rstrip()
moves = list(map(int, input().split()))

map_graph = {
    0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: [6, 10], 
    6: 7, 7: 8, 8: 9, 9: 26, # 9 -> 25
    10: 11, 11: 12, 12: 13, 13: 14, 14: [15, 18],
    15: 16, 16: 9, 
    18: 19, 19: 20, 20: 21, 21: 22, 22: [23, 29],
    23: 24, 24: 25, 25: 9,
    26: 27, 27: 28,
    29: 30, 30: 31, 31: 32, 32: 28,
    28: 33 # 도착
}

map_score = {
    0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10,
    6: 13, 7: 16, 8: 19, 9: 25,
    10: 12, 11: 14, 12: 16, 13: 18, 14: 20,
    15: 22, 16: 24,
    18: 22, 19: 24, 20: 26, 21: 28, 22: 30,
    23: 28, 24: 27, 25: 26,
    26: 30, 27: 35, 28: 40,
    29: 32, 30: 34, 31: 36, 32: 38,
    33: 0
}

mx = -1

def func(i, nows, score):
    global mx
    
    if i == 10:
        mx = max(score, mx)
        return

    for n, now in enumerate(nows):
        move = moves[i]
        was = now
        while move > 0:   
            if now == 33: # 도착점에 오면 즉시 종료
                break
                
            if type(map_graph[now]) == list:
                if move == moves[i]:
                    now = map_graph[now][0]
                else:
                    now = map_graph[now][1]
            else:
                now = map_graph[now]
    
            move -= 1

        if now < 33 and now in nows: 
            continue       
        
        score += map_score[now]
        nows[n] = now
        func(i+1, nows, score)
        score -= map_score[now]
        nows[n] = was

func(0, [0, 0, 0, 0], 0)

print(mx)