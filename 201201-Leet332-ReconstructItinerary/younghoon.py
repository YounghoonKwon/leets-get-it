from collections import defaultdict 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        data2node = defaultdict(list)
        for fr, to in tickets:
            data2node[fr].append(to)
        for val in data2node.values():
            val.sort()

        result = []
        def dfs(node):
            while data2node[node]:
                dfs(data2node[node].pop(0))
            result.append(node)
        dfs("JFK")
        
        return reversed(result)
        
