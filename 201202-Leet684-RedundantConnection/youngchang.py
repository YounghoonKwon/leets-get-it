class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for u, v in edges:
            n = max(n, u, v)
        
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x, parent):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x], parent)
            return parent[x]

        def union(u, v):
            u = find(u, parent)
            v = find(v, parent)
            if u == v:
                return True
            if rank[u] > rank[v]:
                u, v = v, u
            parent[u] = v
            if rank[u] == rank[v]:
                rank[v] += 1
            return False
        
        for i, (u, v) in enumerate(edges):
            if union(u, v):
                answer = i
        
        return edges[answer]