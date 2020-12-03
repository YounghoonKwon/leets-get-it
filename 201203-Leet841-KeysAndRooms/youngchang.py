class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        seen = set()
        q = [0]
        for node in q:
            if node in seen: continue
            seen.add(node)
            for nei in rooms[node]:
                q.append(nei)

        return list(range(N)) == sorted(seen)