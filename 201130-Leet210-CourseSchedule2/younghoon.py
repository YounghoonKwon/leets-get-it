class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            indegree[pre[0]].add(pre[1])
            outdegree[pre[1]].append(pre[0])
        start, ret = [i for i in range(numCourses) if not indegree[i]], []
        while start: 
            newStart = []
            for i in start:
                ret.append(i)
                for j in outdegree[i]:
                    indegree[j].remove(i)
                    if not indegree[j]:
                        newStart.append(j)
            start = newStart
        return ret if len(ret) == numCourses else []
