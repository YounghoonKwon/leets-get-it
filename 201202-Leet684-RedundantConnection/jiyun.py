class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v: -1 for v in range(1, len(edges) + 1)}
        def find(u):
            if parent[u] != -1:
                parent[u] = find(parent[u])
                return parent[u]
            else: return u
            
        def union(u, v):
            parentOfU = find(u)
            parentOfV  = find(v)
            
            if parentOfU == parentOfV: return True # cycle
            else:
                parent[parentOfU] = parentOfV
                return False
        for u, v in edges:
            if union(u,v): return [u,v]
