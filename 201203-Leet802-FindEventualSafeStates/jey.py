class Solution(object):
    def eventualSafeNodes(self, graph):
     
        color = [0] * len(graph)
        res = []
        for start in range(len(graph)):
            if self.dfs(graph, start, color):
                res.append(start)
        res.sort()
        return res
        
    def dfs(self, graph, start, color):
        if color[start] != 0:
            return color[start] == 1
        color[start] = 2
        for e in graph[start]:
            if not self.dfs(graph, e, color):
                return False
        color[start] = 1
        return True
