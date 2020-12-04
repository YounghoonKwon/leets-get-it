class Solution(object):
    def union(self, a, b):
        self.uf[self.find(b)] = self.find(a)

    def find(self, a):
        while self.uf[a] != a:
            a = self.uf[a]
        return a
    
    def detectCycle(self, V):
        self.visited[V] = True
        for i in range(len(self.adjList[V])):
            nextV = self.adjList[V][i]
            if self.visited[nextV]:
                return (V, nextV)
            ret = self.detectCycle(nextV)
            if ret[0]:
                return ret
        return (None, None)
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        self.uf = [0] + [i + 1 for i in range(len(edges))]
        self.adjList = [[] for i in range(len(edges) + 1)]     
        hasFather = [False] * (len(edges) + 1)                 
        criticalEdge = None
        for i, edge in enumerate(edges):
            w, v = edge[0], edge[1]
            self.adjList[w].append(v)
            if hasFather[v]:
                criticalEdge = (w, v)        
            hasFather[v] = True
            if self.find(w) == self.find(v):
                cycleEdge = (w, v)
            self.union(w, v)
        if not criticalEdge:       
            return cycleEdge
        self.visited = [False] * (len(edges) + 1)
        (w, v) = self.detectCycle(criticalEdge[1])
        return (w, v) if w else criticalEdge     
