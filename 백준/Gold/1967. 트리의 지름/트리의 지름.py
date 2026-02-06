import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
# 간선이 연결하는 두 노드 중 부모 노드 번호, 자식 노드, 간선의 가중치
edges = defaultdict(set)
edge_ws = {}
for e in range(n-1):
    p, c, w = map(int, input().split())
    edges[p].add(c)
    edges[c].add(p)
    u, v = sorted([p, c])
    edge_ws[(u, v)] = w
    
def func(N):
    dist = [0]*n # dist[x-1]
    dfs = [N]
    vis = set()
    
    while dfs:
        frm = dfs.pop()
        vis.add(frm)
        
        for to_visit in edges[frm]:
            if to_visit in vis:
                continue
    
            f, t = sorted([frm, to_visit])
            dist[to_visit-1] = dist[frm-1] + edge_ws[(f, t)]
            dfs.append(to_visit)

    return dist

from_one = func(1)
mx = max(from_one)
mx_idx = from_one.index(mx)+1
from_mx = func(mx_idx)

print(max(from_mx))