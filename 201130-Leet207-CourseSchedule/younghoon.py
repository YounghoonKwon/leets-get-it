class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegree[pre[0]].add(pre[1])
            outdegree[pre[1]].append(pre[0])
        start, count = [i for i in range(numCourses) if not indegree[i]], 0
        while start: 
            newStart = []
            for i in start:
                count += 1
                for j in outdegree[i]:
                    indegree[j].remove(i)
                    if not indegree[j]:
                        newStart.append(j)
            start = newStart
        return count == numCourses
