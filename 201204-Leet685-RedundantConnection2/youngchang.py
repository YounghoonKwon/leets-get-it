class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for u, v in edges:
            n = max(n, u, v)
        
        ind = [0] * (n + 1)
        graph = defaultdict(list)
        for u, v in edges:
            ind[v] += 1
            graph[u].append(v)
        
        def topo(ind, graph):
            cnt = 0
            q = [i for i in range(1, n + 1) if ind[i] == 0]
            if len(q) != 1: return False
            while q:
                node = q.pop()
                cnt += 1
                for nei in graph[node]:
                    ind[nei] -= 1
                    if ind[nei] == 0:
                        q.append(nei)
            
            return cnt == n
        
        for u, v in edges[::-1]:
            ind[v] -= 1
            graph[u].remove(v)
            if topo(ind.copy(), graph):
                return [u, v]
            ind[v] += 1
            graph[u].append(v)
            