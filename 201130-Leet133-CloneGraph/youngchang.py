"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        root_val = node.val
        graph = collections.defaultdict(list)
        q = [node]
        seen = set()
        while q:
            n = q.pop()
            if n.val in seen: continue
            seen.add(n.val)
            for nei in n.neighbors:
                graph[n.val].append(nei.val)
                q.append(nei)
        
        nodes = [Node(i) for i in range(101)]
        for key, vals in graph.items():
            curr = nodes[key]
            curr.neighbors = []
            for nei in vals:
                curr.neighbors.append(nodes[nei])
                
        return nodes[root_val]