class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: (x[0], x[1]))
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

        i = answer = 0
        while i < len(ranges):
            answer += 1 
            s, e = ranges[i]
            par = i
            i += 1
            while i < len(ranges) and e >= ranges[i][0]:
                union(par, i)
                if e < ranges[i][1]:
                    e = ranges[i][1]
                i += 1

                
        return 2 ** answer % (10 ** 9 + 7)