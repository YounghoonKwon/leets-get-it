class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        graph = collections.defaultdict(list)
        for second, first in prerequisites:
            ind[second] += 1
            graph[first].append(second)

        q = [i for i in range(numCourses) if ind[i] == 0]
        cnt = 0
        while q:
            node = q.pop()
            cnt += 1
            for nei in graph[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        
        return cnt == numCourses