from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        len_logs = len(logs)
        logs.sort(key=lambda x: x[1])
        std_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])
        answer = [0]*len(queries)

        # initial values
        active = defaultdict(int)
        left = right = 0
        cnt = 0

        for query, i in std_queries:
            while right < len_logs and logs[right][1] <= query:
                server = logs[right][0]
                if active[server] == 0:
                    cnt += 1
                active[server] += 1
                right += 1
            
            while left < len_logs and logs[left][1] < query-x:
                server = logs[left][0]
                active[server] -= 1
                if active[server] == 0:
                    cnt -= 1
                left += 1
            
            answer[i] = n - cnt
        
        return answer