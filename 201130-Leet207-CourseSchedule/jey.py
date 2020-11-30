class Solution:
    def canFinish(self, numCourses, prerequisites):
        def dfs(vertex):
            if visited[vertex]:
                return True
            if visited[vertex] == False:
                return False
            visited[vertex] = False
            for prerequisite in graph[vertex]:
                if not dfs(prerequisite):
                    return False
            visited[vertex] = True
            return True

        visited = [None]*numCourses
        graph = [list() for _ in range(numCourses)]

        for vertex, prerequisite in prerequisites:
            graph[vertex].append(prerequisite)

        for vertex in range(numCourses):
            if not dfs(vertex):
                return False

        return True
