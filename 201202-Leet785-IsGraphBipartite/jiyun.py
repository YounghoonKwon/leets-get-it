class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        color = [set(), set()]
        
        for i in range(len(graph)):
            if not i in visited:
                queue = [(i, 0)]
                while queue:
                    node, level = queue.pop()
                    visited.add(node)
                    color[level].add(node)
                    
                    for nei in graph[node]:
                        if nei in color[level]: return False
                        if not nei in visited:
                            queue.append((nei, 1 if level == 0 else 0))
        return True
