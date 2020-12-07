class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        while k:
            answer = -heappop(nums)
            k -= 1
        return answer