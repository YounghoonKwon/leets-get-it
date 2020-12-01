from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]
            
        def dfs(fr, to, visited):
            if fr not in graph or to not in graph: return -1
            if to in graph[fr]:
                return graph[fr][to]
            
            for i in graph[fr]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,to,visited)
                    if temp == -1:
                        continue
                    return temp * graph[fr][i]
            return -1
        
        output = []
        for p, q in queries:
            output.append(dfs(p,q,set()))
        return output
