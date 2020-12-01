class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(city):
            while(len(graph[city]) > 0):
                dfs(graph[city].pop())
            initery.insert(0, city)
        graph = collections.defaultdict(list)
        for i, t in tickets:
            graph[i].append(t)
            graph[i].sort(reverse=True)
        initery = []
        dfs("JFK")
        return initery
