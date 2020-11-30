from collections import deque

class Solution:
    def makeAdjList(self, numCourses, prerequisites):
        list=[[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            b,a = prerequisite
            list[a].append(b)
        return list
    
    def isCyclic(self, numCourses, prerequisites, adjList):
        visited = [False for _ in range(numCourses)]
        q= deque()
        def adj(course, stack):
            for i in adjList[course]:
                if adj(i, stack):
                    return True
            
            visited[course] = True
            if len(q) != numCourses and course not in visited:
                q.append(course)
                
            return False
            
        for course in range(numCourses):
            path = adj(course, set())
            if path:
                return True
        
        print('visited', visited)
        return False, q
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = self.makeAdjList(numCourses, prerequisites)
        print('ad', adjList)
        
        
        dag, q = self.isCyclic(numCourses, prerequisites, adjList)
        if dag:
            return []
        else:
            return [q.pop() for _ in range(len(q))]   
