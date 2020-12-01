class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        
        for (dividend, divisor), val in zip(equations, values):
            graph[dividend][divisor] = val
            graph[divisor][dividend] = 1 / val
        
        def bfs(dividend, divisor):
            q = [(dividend, 1, set())]
            for curr, acc, seen in q:
                if curr == divisor: return acc
                for nei, mul in graph[curr].items():
                    if nei in seen: continue
                    q.append((nei, acc * mul, seen | {nei}))
            return -1
        
        answer = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                answer.append(-1)
            elif dividend == divisor:
                answer.append(1)
            else:
                answer.append(bfs(dividend, divisor))

        return answer