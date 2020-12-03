'''요고어렵네요 ㅠㅠ'''

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            visited[node] = 0
            for v in graph[node]:
                if visited[v] == 0 or (visited[v] == -1 and dfs(v)): 
                    return True
            visited[node] = 1
            result.append(node)
            return False
        
        visited = [-1] * len(graph) 
        result = []
        for i in range(len(graph)):
            if visited[i] == -1: 
                dfs(i)
        return sorted(result)
