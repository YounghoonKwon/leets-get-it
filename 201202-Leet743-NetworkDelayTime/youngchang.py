class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
            
        time_memo = {i: float('inf') for i in range(1, N + 1)}
        time_memo[K] = 0
        
        q = [(0, K)]
        while q:
            time, node = heappop(q)
            for nei, w in graph[node].items():
                if time + w < time_memo[nei]:
                    time_memo[nei] = time + w
                    heappush(q, (time + w, nei))
        
        max_time = max(time_memo.values())
        return max_time if max_time != float('inf') else -1