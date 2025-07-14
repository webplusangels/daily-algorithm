import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
eggs = []

for _ in range(N):
    hp, weight = map(int, input().split())
    eggs.append((hp, weight))

max_eggs = 0
broken = [hp[0] for hp in eggs]

def func(holding):
    global max_eggs
    # holding이 N의 길이만큼 오면 종료
    if holding == N:
        max_eggs = max(max_eggs, len([egg for egg in broken if egg <= 0]))
        return

    # 만약 들고 있는 달걀이 깨지면 return
    if broken[holding] <= 0:
        func(holding+1)
        return

    flag = False
    
    # 반복문
    for i in range(N):
        # 같은 달걀이거나, 이미 깨진 달걀이면 continue
        if i == holding or broken[i] <= 0:
            continue

        flag = True
        # 깨고 다음 달걀로 이동
        broken[i] -= eggs[holding][1]
        broken[holding] -= eggs[i][1]
        func(holding+1)
        broken[i] += eggs[holding][1]
        broken[holding] += eggs[i][1]

    if not flag:
        func(holding+1)
        
func(0)
print(max_eggs)