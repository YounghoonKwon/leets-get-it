class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
            
        dist = {node: float('inf') for node in range(1, N + 1)}
            
        def dfs(node, passed):
            if passed >= dist[node]: return
            dist[node] = passed
            for time, nei in sorted(graph[node]):
                dfs(nei, passed + time)
        dfs(K, 0)
        ans = max(dist.values())
        print(dist)
        return ans if ans < float('inf') else -1
    
