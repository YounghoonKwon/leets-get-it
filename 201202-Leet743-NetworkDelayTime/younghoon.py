class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = collections.defaultdict(list)
        for u, v, cost in times:
            g[u].append((cost,v))
        
        min_heap = [(0, K)] # cost, u
        visited = set()
        distance = {i:float('inf') for i in range(1, N+1)}
        distance[K] = 0
        while min_heap:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            if len(visited) == N: # Found!
                return cost
            
            for cost2, v in g[u]:
                if cost + cost2 < distance[v] and v not in visited:
                    distance[v] = cost + cost2
                    heapq.heappush(min_heap, (cost + cost2, v))
        return -1
