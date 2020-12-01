class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def bfs(st):
            q = [(st, 0)]
            seen = set()
            for node, dist in q:
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen:
                        q.append((nei, dist + 1))
            return node, dist
        
        def bfs2(st, target_depth):
            q = [(st, 0)]
            seen = set()
            answer = []
            for node, dist in q:
                if dist == target_depth:
                    answer.append(node)
                elif dist > target_depth:
                    break
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen:
                        q.append((nei, dist + 1))
            return answer
        
        root, _ = bfs(0)
        leaf, diameter = bfs(root)
        min_depth = (diameter + 1) // 2
        cand = set(bfs2(leaf, min_depth) + bfs2(root, min_depth))
        answer = []
        for node in cand:
            _, dist = bfs(node)
            if dist == min_depth:
                answer.append(node)
        
        return answer