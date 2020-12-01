class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge = [set() for _ in range(n)]
        for u, v in edges:
            edge[u].add(v)
            edge[v].add(u)
        q = [x for x in range(n) if len(edge[x]) < 2]
        tmp = []
        while True:
            for node in q:
                for n in edge[node]:
                    edge[n].remove(node)
                    if len(edge[n]) == 1:
                        tmp.append(n)
            if not tmp:
                break
            tmp, q = [], tmp
        return q
