class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safety = {}
        visited = set()
        def dfs(node):
            if node in safety:
                return safety[node]
            
            safety[node] = True
            visited.add(node)
            for i in graph[node]:
                i in visited or not dfs(i):
                    safety[node] = False
                    returnif 
            visited.remove(node)
            return safety[node]
        return [ n for n in range(len(graph)) if dfs(n)]
        
