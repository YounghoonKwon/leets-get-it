class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = dict(zip(range(1, n + 1), range(1, n + 1)))
        last = candidate = None
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for v, w in edges:
            if parent[w] != w:
                candidate = [v, w]
                continue
            if root(v) == w: #cycle
                last = [v, w]
                continue
            parent[w] = v
            n -= 1
        return [parent[candidate[1]], candidate[1]] if n > 1 else (candidate or last)
