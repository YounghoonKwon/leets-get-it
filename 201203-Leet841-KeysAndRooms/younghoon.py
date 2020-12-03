class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(rooms,node):
            visited[node] = True
            for i in rooms[node]:
                if visited[i] == False:
                    dfs(rooms,i)
                    
        visited = [False for i in range(len(rooms))]
        dfs(rooms,0)
        
        for i in visited:
            if not i:
                return False
        return True

