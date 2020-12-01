class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return edges[0] if n != 1 else [0]
        
        nodes = [set() for i in range(n)]
        for start, end in edges:
            nodes[start].add(end);
            nodes[end].add(start);
            
        leaves = []
        for i in range(n):
            if len(nodes[i]) == 1:
                leaves.append(i)
                
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                node = nodes[leaf].pop()
                nodes[node].remove(leaf)
                if len(nodes[node]) == 1:
                    new_leaves.append(node)
                    
            leaves = new_leaves
        return leaves
