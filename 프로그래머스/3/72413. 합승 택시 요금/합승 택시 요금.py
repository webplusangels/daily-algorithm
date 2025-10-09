from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    # S에서 A와 B를 제외한 다른 지점으로 갈 때 최소 거리 + 그 지점에서 A와 B로 가는 거리
    # A와 B로 각자 가는 거리를 합해서 비교
    graphs = defaultdict(list)
    for f in fares:
        graphs[f[0]].append((f[1], f[2]))
        graphs[f[1]].append((f[0], f[2]))
        
    def dijkstra(start):
        distances = {node+1: float('inf') for node in range(n)}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > distances[node]:
                continue
                
            for to_node, to_dist in graphs[node]:
                updated = dist + to_dist
                if distances[to_node] > updated:
                    distances[to_node] = updated
                    heapq.heappush(pq, (updated, to_node))
        
        return distances
    
    dists_s = dijkstra(s)
    dists_a = dijkstra(a)
    dists_b = dijkstra(b)
    
    answer = float('inf')
    for i in range(1, n+1):
        result = dists_s[i] + dists_a[i] + dists_b[i]
        answer = min(answer, result)
        
    return answer