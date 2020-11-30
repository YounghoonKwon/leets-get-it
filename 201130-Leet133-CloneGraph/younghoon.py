import copy
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        visited = {}
        def dfs(node, visited):
            new_node = Node(node.val)
            visited[node.val] = new_node
            new_neighbors = []
            for n in node.neighbors:
                if n.val not in visited:
                    new_neighbors.append(dfs(n,visited))
                else:
                    new_neighbors.append(visited[n.val])
            new_node.neighbors = new_neighbors
            return new_node
        
        return dfs(node, visited)
