import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# 상위 폴더의 이름, 폴더 혹은 파일의 이름, 폴더인가
directories = [input().split() for _ in range(N+M)]

Q = int(input())
queries = [input() for _ in range(Q)]

# 한 번에 그래프를 만들기
graph = defaultdict(list)
files = defaultdict(list)
for directory in directories:
    p, f, c = directory
    graph[p].append([f, c])
    
# 그 후에 계산
for query in queries:
    where = query.split('/')
    dq = deque([where[-1]])
    fls, cnt = set(), 0
    while dq:
        w = dq.popleft()
        for f, c in graph[w]:
            if c == '1':
                dq.append(f)
            else:
                fls.add(f)
                cnt += 1
                
    print(len(fls), cnt)