class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        ind = [len(i) for i in graph]
        parent = defaultdict(list)
        for node, children in enumerate(graph):
            for child in children:
                parent[child].append(node)
        
        safe = []
        q = [i for i in range(N) if ind[i] == 0]
        while q:
            node = q.pop()
            safe.append(node)
            for p in parent[node]:
                ind[p] -= 1
                if ind[p] == 0:
                    q.append(p)
        
        return sorted(safe)