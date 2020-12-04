class DisjointSet: #(UnionFind)
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        self.parent[x] = self.parent[y]
        return True
    
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        cand1, cand2, point_to = None, None, {}
        for node1, node2 in edges:
            if node2 in point_to: 
                cand1, cand2 = point_to[node2], [node1, node2]
                break
            point_to[node2] = [node1, node2]
            
        ds = DisjointSet(len(edges))
        for node1, node2 in edges:
            if [node1, node2] == cand2: continue
            if not ds.union(node1 - 1, node2 - 1):
                if cand1: return cand1
                return [node1, node2]
        return cand2
