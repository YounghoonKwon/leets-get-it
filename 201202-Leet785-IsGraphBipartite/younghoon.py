class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        
        def dfs(u, c):
            color[u] = c
            for v in graph[u]:
                if color[v] == c: return False
                elif not color[v] and not dfs(v, -c): return False
            return True

        for i in range(n):
            if not color[i]:
                if not dfs(i, 1):
                    return False
        return True
