class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for i, neighbors in enumerate(graph):
            adj[i].update(neighbors)
            
        all_nodes = set(range(len(graph)))
        grouped = set()
            
        def get_group(elem):
            seen = set()
            q = [elem]
            for node in q:
                if node in seen: continue
                seen.add(node)
                for nei in adj[node]:
                    q.append(nei)
            nonlocal grouped
            grouped |= seen
            return seen
        
        def is_valid_group(A):
            for node in A:
                set1 = A - adj[node]
                set2 = A - set1

                found = True
                for elem in set1:
                    if set1 & adj[elem]:
                        found = False
                        break
                if not found: continue
                for elem in set2:
                    if set2 & adj[elem]:
                        found = False
                        break
                if found:
                    return True

            return False
        
        for node in all_nodes:
            if node not in grouped:
                group = get_group(node)
                if is_valid_group(group) == False:
                    return False
        return True