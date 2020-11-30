class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        idToNode = {} # store reference based on node id
        return self.clone(node, idToNode)   
    
    def clone(self, node: 'Node', hashmap: map) -> 'Node':
        if not node:
            return None
        
        if node.val in hashmap: # already visited aka cloned the node with the id in val
            return hashmap[node.val]
        
        cloned = Node(node.val, [])
        hashmap[node.val] = cloned
       
        for neighbor in node.neighbors:
            cloned.neighbors.append(self.clone(neighbor, hashmap))
        
        return cloned
