class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last = len(graph) - 1
        answer = []
        q = [(0, [0])]
        for node, path in q:
            if node == last:
                answer.append(path)
                continue
            for nei in graph[node]:
                q.append((nei, path + [nei]))
        
        return answer