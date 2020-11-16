class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1+nums2)
        size = len(arr)
        if size % 2 == 0:
            # even
            return (arr[int(size/2)] + arr[int(size/2 - 1)]) / 2
        else:
            # odd
            return arr[int((size - 1) / 2)]
