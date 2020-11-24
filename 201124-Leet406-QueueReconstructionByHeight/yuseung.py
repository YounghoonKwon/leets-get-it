class Solution(object):
    def reconstructQueue(self, people):
        ans = []
        heap = []
        for p in people:
            heapq.heappush(heap, [-p[0], p[1]])
        while heap:
            hi = heapq.heappop(heap)
            ans.insert(hi[1], [-hi[0], hi[1]])
        return ans
