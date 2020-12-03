class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visit = [0]*N
        stack = [0]
        while stack:
            u = stack.pop()
            visit[u] = 1
            neighbors = rooms[u]
            for n in neighbors:
                if not visit[n]:
                    stack.append(n)
        return not 0 in visit 
