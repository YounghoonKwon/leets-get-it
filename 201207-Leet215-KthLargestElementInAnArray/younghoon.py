
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        result = 0;
        for _ in range(k):
            result = heapq._heappop_max(nums)
            print(result)
        return result;
        
