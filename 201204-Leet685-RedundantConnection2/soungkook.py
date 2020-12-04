class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = dict(zip(range(1,n+1), range(1,n+1)))
        last_cycle_edge = candidate_edge = candidate = None
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for e in edges:
            v, w = e
            if parent[w] != w: # case 1: w has 2 parents
                candidate_edge, candidate = e, w
                continue
            if root(v) == w: # case 2: [v, w] makes a cycle
                last_cycle_edge = e
                continue
            parent[w], n = v, n-1
        return [parent[candidate], candidate] if n > 1 else (candidate_edge or last_cycle_edge)
