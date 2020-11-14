class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) %2 == 1:
            return float(nums3[len(nums3)//2])
        else:
            return float(nums3[len(nums3)//2] + nums3[len(nums3)//2-1])/2
