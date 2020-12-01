class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(dep):
            arr = paths[dep]
            while arr:
                dfs(arr.pop())
            res.append(dep)

        res = []
        paths = defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse=True)
        for s, t in tickets:
            paths[s].append(t)
        dfs('JFK')
        return res[::-1]
