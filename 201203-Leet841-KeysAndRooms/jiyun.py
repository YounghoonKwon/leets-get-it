class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = [False] * len(rooms)
        opened[0] = True
        stack = [0]
        
        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not opened[nei]:
                    opened[nei] = True
                    stack.append(nei)
        return all(opened)
                    
