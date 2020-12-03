class Solution:
    def allPathsSourceTarget(self, graph):
		
        res = []
        q = []
        q.append([0,[]])
        n = len(graph)
        
        while q:
            tempNode, route = q.pop(0)
            
            if tempNode == n - 1:
                res.append(route + [tempNode])
                continue
            
            for neighbor in graph[tempNode]:
                q.append([neighbor, route + [tempNode]])
        
        return res
