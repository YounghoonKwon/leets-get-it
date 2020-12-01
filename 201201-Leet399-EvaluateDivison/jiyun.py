class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, end):
            if not (start in graph and end in graph):
                return -1.0
            queue = [(start, 1.0)]
            visited = set()
            
            while queue:
                y, val = queue.pop()
                if y == end: return val
                
                visited.add(y)
                for i, v in graph[y].items():
                    if not i in visited:
                        queue.append((i, val * v))
            return -1.0
        
        graph = collections.defaultdict(defaultdict)
        for (v1, v2), val in zip(equations, values):
            graph[v1][v2] = val
            graph[v2][v1] = 1/val\
            
        res = []
        for start, end in queries:
            res.append(dfs(start, end))
            
        return res
