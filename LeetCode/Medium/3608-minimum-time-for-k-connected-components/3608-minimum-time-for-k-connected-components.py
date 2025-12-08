class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key = lambda x: -x[2])
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            xx, yy = find(x), find(y)
            if xx != yy:
                parent[xx] = yy

        now = n

        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                continue
            
            if now - 1 < k:
                return edge[2]
            
            union(edge[0], edge[1])
            now -= 1
        else:
            return 0