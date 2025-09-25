import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dates = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    dates.append((tmp[0]*100 + tmp[1], tmp[2]*100 + tmp[3]))
    
dates.sort()

i = cnt = 0
current = 301

# current보다 작은 값으로 출발하는 tuple을 최대한 찾아
# 그 다음 가장 큰 값을 저장하는것
while i < N and current < 1201:
    tmp_max = current
    while i < N and dates[i][0] <= current:
        tmp_max = max(tmp_max, dates[i][1])
        i += 1
    if current != tmp_max:    
        current = tmp_max
        cnt += 1
    else:
        cnt = 0
        break

if current < 1201:
    cnt = 0
    
print(cnt)