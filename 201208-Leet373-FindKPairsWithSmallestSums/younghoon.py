import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        pq = []
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(pq, [n1+n2, (n1,n2)])
        
        result = []
        for i in range(k):
            if not pq:
                break
            result.append(list(heapq.heappop(pq)[1]))
        return result
