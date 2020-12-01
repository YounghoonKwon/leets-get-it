from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        data2node = defaultdict(list)
        degree = [0] * n
        
        for e in edges:
            data2node[e[0]].append(e[1])
            data2node[e[1]].append(e[0])
            degree[e[0]] += 1
            degree[e[1]] += 1
            
        queue = [ n for n in range(n) if degree[n]==1 ]
        
        if n <= 2:
            return queue
        
        while queue:
            nextleaf = []
            result = queue
            for leaf in queue:
                for adj in data2node[leaf]:
                    degree[adj] -= 1
                    if degree[adj] == 1:
                        nextleaf.append(adj)
            queue = nextleaf
        return result
