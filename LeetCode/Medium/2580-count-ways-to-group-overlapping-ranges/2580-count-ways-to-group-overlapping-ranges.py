class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: (x[0], x[1]))
        print(ranges)
        parent = [n for n in range(len(ranges))]

        def find(x):
            if parent[x] == x:
                return x
            
            return find(parent[x])
        
        def union(x, y):
            p_x, p_y = find(x), find(y)

            if p_x == p_y:
                return

            if p_x < p_y:
                parent[p_y] = p_x
            else:
                parent[p_x] = p_y

        i = 0
        while i < len(ranges):
            s, e = ranges[i]
            par = i
            i += 1
            while i < len(ranges) and e >= ranges[i][0]:
                union(par, i)
                if e < ranges[i][1]:
                    e = ranges[i][1]
                i += 1
                
        
        print([find(x) for x in range(len(ranges))])
        return 2 ** len(set(parent))