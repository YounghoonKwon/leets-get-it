class Solution(object):
    def calcEquation(self, equations, values, queries):
        
        def dfs(start, end, path, paths):
            if start == end and start in G:
                paths[0] = path
                return
            if start in vis: 
                return
            vis.add(start)
            for node in G[start]:
                dfs(node, end, path * W[start, node], paths)
        
        
        G, W = collections.defaultdict(set), collections.defaultdict(float)
        for (A, B), V in zip(equations, values):
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0 / V
            
        res = []
        for X, Y in queries:
            paths, vis = [-1.0], set()
            dfs(X, Y, 1.0, paths)
            res += paths[0],
        return res
