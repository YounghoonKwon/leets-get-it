class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack = [('JFK', tickets, ['JFK'])]
        while stack:
            dptr, remain, path = stack.pop()
            if not remain:
                return path
            for arrv in sorted([ed for st,ed in remain if st==dptr], reverse=True):
                temp = remain.copy()
                temp.remove([dptr,arrv])
                stack.append((arrv, temp, path+[arrv]))