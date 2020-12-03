class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        routes = []
        partial = [0]
        def dfs(node):
            if node == len(graph) - 1:
                routes.append(partial.copy())
                return
        
            for i in graph[node]:
                partial.append(i)
                dfs(i)
                partial.pop()
        dfs(0)
        return routes
