class Solution(object):
   def findOrder(self, numCourses, prerequisites):
      in_degree,adj=self.create_adj(numCourses,prerequisites)
      visited = [0 for i in range(numCourses)]
      stack = []
      for i in range(numCourses):
         if not visited[i] and not self.dfs(i,visited,stack,adj):
            return []
      return stack[::-1]
   def create_adj(self,n,graph):
      adj = {}
      in_degree= [0 for i in range(n)]
      for i in graph:
         in_degree[i[0]]+=1
         if i[1] in adj:
            adj[i[1]].append(i[0])
         else:
            adj[i[1]] = [i[0]]
      return in_degree,adj
   def dfs(self, node, visited,stack,adj):
      if visited[node] == -1:
         return False
      if visited[node] == 1:
         return True
      visited[node] = -1
      if node in adj:
         for i in adj[node]:
            if not self.dfs(i,visited,stack,adj):
               return False
      visited[node]=1
      stack.append(node)
      return True
ob = Solution()
print(ob.findOrder(2, [[1,0]]))
