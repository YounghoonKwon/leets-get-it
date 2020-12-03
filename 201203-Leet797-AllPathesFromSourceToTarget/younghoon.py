class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph) - 1
        def dfs(node, path, output):
            if node == dest:
                output.append(path)
            for next_node in graph[node]:
                dfs(next_node, path+[next_node], output)
                
        output = []
        dfs(0,[0],output)
        return output
